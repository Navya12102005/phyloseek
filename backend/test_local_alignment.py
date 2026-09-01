from smith_waterman import smith_waterman

# These two sequences are mostly different, but share "GGCCATT" in the middle
seq1 = "TTTTGGCCATTCCCC"
seq2 = "AAAAGGCCATTGGGG"

a1, a2, score = smith_waterman(seq1, seq2)
print("Local alignment 1:", a1)
print("Local alignment 2:", a2)
print("Score:", score)