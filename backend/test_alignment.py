from needleman_wunsch import needleman_wunsch

# Small test with real-ish looking sequences
seq1 = "ATGGCCATTGTAATGGGCCGCTGA"
seq2 = "ATGGCCATTGTAATGGGCCGCTAA"

a1, a2, score = needleman_wunsch(seq1, seq2)
print("Sequence 1 aligned:", a1)
print("Sequence 2 aligned:", a2)
print("Score:", score)

# Count matches, mismatches, gaps for a simple summary
matches = sum(1 for x, y in zip(a1, a2) if x == y)
gaps = a1.count('-') + a2.count('-')
print(f"\nMatches: {matches}/{len(a1)}")
print(f"Gaps: {gaps}")