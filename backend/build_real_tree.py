from fetch_data import fetch_uniprot
from needleman_wunsch import needleman_wunsch
from Bio import Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

def clean_fasta(fasta_text):
    """Extract just the sequence, removing the header line."""
    lines = fasta_text.strip().split("\n")
    return "".join(lines[1:])  # skip header, join sequence lines

species_ids = {
    "Human": "P04637",
    "Mouse": "P02340",
}

# Fetch and clean sequences
sequences = {}
for species, uid in species_ids.items():
    raw = fetch_uniprot(uid)
    sequences[species] = clean_fasta(raw)
    print(f"{species}: {len(sequences[species])} amino acids")

# Align Human vs Mouse using YOUR Needleman-Wunsch
a1, a2, score = needleman_wunsch(sequences["Human"], sequences["Mouse"], match=1, mismatch=-1, gap=-2)
print(f"\nAlignment score: {score}")
print(f"Human aligned (first 80): {a1[:80]}")
print(f"Mouse aligned (first 80): {a2[:80]}")

matches = sum(1 for x, y in zip(a1, a2) if x == y)
print(f"\nMatches: {matches}/{len(a1)} ({100*matches/len(a1):.1f}% identity)")
