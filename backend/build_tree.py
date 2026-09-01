from Bio import Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

# Example: a few related sequences (placeholder data for now)
records = [
    SeqRecord(Seq("ATCGTACGTA"), id="Human"),
    SeqRecord(Seq("ATCGTATGTA"), id="Chimp"),
    SeqRecord(Seq("ATGGTACGTA"), id="Mouse"),
    SeqRecord(Seq("ATCGTACGTT"), id="Rat"),
]

alignment = MultipleSeqAlignment(records)

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
print("Distance matrix:")
print(distance_matrix)

constructor = DistanceTreeConstructor()
tree = constructor.nj(distance_matrix)  # neighbor-joining tree

print("\nTree structure (text format):")
Phylo.draw_ascii(tree)