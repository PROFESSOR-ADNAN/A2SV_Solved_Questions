def query(prefix, r1, c1, r2, c2):
    ans = prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1]

    return ans

for r1, c1, r2, c2 in queries:
    horizontal = query(horzontalPlacementPrefix, r1, c1, r2, c2-1)
    vertical = query(verticalPlacementPrefix, r1, c1, r2-1, c2)

    ans = horizontal + vertical

    print(ans)