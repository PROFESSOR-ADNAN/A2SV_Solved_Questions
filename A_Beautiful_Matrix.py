# matrix = [list(map(int, input().split())) for i in range(5)]

# Row = len(matrix)
# Col = len(matrix[0])

# for r in range(Row):
#     for c in range(Col):
#         if matrix[r][c] == 1:
#             print(abs(r-c))
#             break


matrix = [list(map(int, input().split())) for i in range(5)]

Row = len(matrix)
Col = len(matrix[0])

for r in range(Row):
    for c in range(Col):
        if matrix[r][c] == 1:
            print(abs(r-2) + abs(c-2))
            break


