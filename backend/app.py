from flask import Flask, render_template, request
from fetch_data import fetch_genbank, fetch_uniprot, fetch_pdb
from needleman_wunsch import needleman_wunsch
from smith_waterman import smith_waterman

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        seq1 = request.form.get("seq1", "").strip().upper()
        seq2 = request.form.get("seq2", "").strip().upper()
        algorithm = request.form.get("algorithm")

        if not seq1 or not seq2:
            error = "Please enter both sequences."
        else:
            try:
                if algorithm == "global":
                    a1, a2, score = needleman_wunsch(seq1, seq2)
                else:
                    a1, a2, score = smith_waterman(seq1, seq2)

                matches = sum(1 for x, y in zip(a1, a2) if x == y)
                identity = round(100 * matches / len(a1), 1) if len(a1) > 0 else 0

                result = {
                    "align1": a1,
                    "align2": a2,
                    "score": score,
                    "matches": matches,
                    "length": len(a1),
                    "identity": identity,
                    "algorithm": "Global (Needleman-Wunsch)" if algorithm == "global" else "Local (Smith-Waterman)"
                }
            except Exception as e:
                error = f"Alignment error: {e}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)