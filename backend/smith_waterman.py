def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-2):
    n, m = len(seq1), len(seq2)
    score = [[0] * (m + 1) for _ in range(n + 1)]

    max_score = 0
    max_pos = (0, 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete_score = score[i-1][j] + gap
            insert_score = score[i][j-1] + gap
            score[i][j] = max(0, match_score, delete_score, insert_score)

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_pos = (i, j)

    # Traceback from the highest-scoring cell, stop when score hits 0
    align1, align2 = "", ""
    i, j = max_pos
    while i > 0 and j > 0 and score[i][j] != 0:
        current = score[i][j]
        if current == score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif current == score[i-1][j] + gap:
            align1 = seq1[i-1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j-1] + align2
            j -= 1

    return align1, align2, max_score