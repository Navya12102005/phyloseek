from fetch_data import fetch_uniprot
from needleman_wunsch import needleman_wunsch
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

def clean_fasta(fasta_text):
    lines = fasta_text.strip().split("\n")
    return "".join(lines[1:])

species_ids = {
    "Human": "P04637",
    "Mouse": "P02340",
    "Chicken": "P10360",
}

# Fetch and clean all sequences
sequences = {}
for species, uid in species_ids.items():
    raw = fetch_uniprot(uid)
    sequences[species] = clean_fasta(raw)
    print(f"{species}: {len(sequences[species])} amino acids")

# Compute pairwise alignment identity using YOUR Needleman-Wunsch
names = list(species_ids.keys())
identity_matrix = {}

print("\nPairwise alignments:")
for i in range(len(names)):
    for j in range(i):
        s1, s2 = names[i], names[j]
        a1, a2, score = needleman_wunsch(sequences[s1], sequences[s2], match=1, mismatch=-1, gap=-2)
        matches = sum(1 for x, y in zip(a1, a2) if x == y)
        identity = matches / len(a1)
        identity_matrix[(s1, s2)] = identity
        print(f"{s1} vs {s2}: {identity*100:.1f}% identity (score {score})")

# Build a distance matrix for tree construction (distance = 1 - identity)
matrix_rows = []
for i, name_i in enumerate(names):
    row = []
    for j in range(i + 1):
        if i == j:
            row.append(0.0)
        else:
            name_j = names[j]
            key = (name_i, name_j) if (name_i, name_j) in identity_matrix else (name_j, name_i)
            row.append(round(1 - identity_matrix[key], 4))
    matrix_rows.append(row)

dm = DistanceMatrix(names, matrix_rows)
print("\nDistance matrix (built from YOUR alignment results):")
print(dm)

constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)

print("\nPhylogenetic tree:")
Phylo.draw_ascii(tree)