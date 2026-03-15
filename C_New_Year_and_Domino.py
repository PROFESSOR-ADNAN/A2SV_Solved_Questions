# h, w = list(map(int, input().split()))
# grid = [input() for _ in range(h)]
# q = int(input())
# queries = [list(map(int, input().split())) for _ in range(q)]


# newGrid = [[0] * w for _ in range(h)]
# for r in range(h):
#     for c in range(w):
#         if grid[r][c] == ".":
#             newGrid[r][c] = 1
#         else:
#             newGrid[r][c] = 0

# prefix = [[0] * (w+1) for _ in range(h+1)]

# for r in range(h):
#     for c in range(w):
#         prefix[r+1][c+1] = prefix[r][c+1] + prefix[r+1][c] - prefix[r][c] + newGrid[r][c]

# # for i in range(h+1):
# #     print(prefix[i])

# # r1, c1, r2, c2 = queries[0][0], queries[0][1], queries[0][2], queries[0][3]
# # ans = prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1]

# # print(ans)

# # . as 0 and # as 1

# # [0, 0, 0, 0, 0, 0, 0, 0, 0]
# # [0, 0, 0, 0, 0, 1, 1, 1, 2]
# # [0, 0, 1, 1, 1, 2, 2, 2, 3]
# # [0, 1, 3, 3, 4, 5, 5, 5, 6]
# # [0, 2, 5, 5, 6, 8, 8, 9, 11]
# # [0, 2, 5, 5, 6, 8, 8, 9, 11]


# # ["0", 0, 0, 0, 1, 1, 1, 2]
# # [0, 1, "1", 1, 2, 2, 2, 3]
# # [1, 3, 3, 4, 5, 5, 5, 6]
# # [2, 5, 5, 6, 8, 8, 9, 11]
# # [2, 5, 5, 6, 8, 8, 9, 11]


# # . as 1 and # as 0


# # [0, 0, 0, 0, 0, 0, 0, 0, 0]
# # [0, 1, 2, 3, 4, 4, 5, 6, 6]
# # [0, 2, 3, 5, 7, 8, 10, 12, 13]
# # [0, 2, 3, 6, 8, 10, 13, 16, 18]
# # [0, 2, 3, 7, 10, 12, 16, 19, 21]
# # [0, 3, 5, 10, 14, 17, 22, 26, 29]


# # ["1", 2, 3, 4, 4, 5, 6, 6]
# # [2, 3, "5", 7, 8, 10, 12, 13]
# # [2, 3, 6, 8, 10, 13, 16, 18]
# # ["2", 3, 7, 10, 12, 16, 19, 21]
# # [3, 5, 10, 14, 17, 22, 26, 29]


# for r1, c1, r2, c2 in queries:
#     ans = prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1]

#     print(ans)





h, w = list(map(int, input().split()))
grid = [input() for _ in range(h)]

horzontalPlacement = [[0] * w for _ in range(h)]
verticalPlacement = [[0] * w for _ in range(h)]

for r in range(h):
    for c in range(w-1):
        if grid[r][c] == "." and grid[r][c+1] == ".":
            horzontalPlacement[r][c] = 1

for r in range(h-1):
    for c in range(w):
        if grid[r][c] == "." and grid[r+1][c] == ".":
            verticalPlacement[r][c] = 1

# for r in range(h):
#     print(*grid[r])

# print()

# for r in range(h):
#     print(*horzontalPlacement[r])

# print()

# for r in range(h):
#     print(*verticalPlacement[r])
    
horzontalPlacementPrefix = [[0] * (w+1) for _ in range(h+1)]
verticalPlacementPrefix = [[0] * (w+1) for _ in range(h+1)]

for r in range(h):
    for c in range(w):
        horzontalPlacementPrefix[r+1][c+1] = horzontalPlacement[r][c] + horzontalPlacementPrefix[r][c+1] + horzontalPlacementPrefix[r+1][c] - horzontalPlacementPrefix[r][c]

for r in range(h):
    for c in range(w):
        verticalPlacementPrefix[r+1][c+1] = verticalPlacement[r][c] + verticalPlacementPrefix[r][c+1] + verticalPlacementPrefix[r+1][c] - verticalPlacementPrefix[r][c]

# for r in range(h):
#     print(*grid[r])

# print()

# for r in range(h):
#     print(*horzontalPlacement[r])

# print()

# for r in range(h):
#     print(*verticalPlacement[r])

# print()

# for r in range(h):
#     print(*horzontalPlacementPrefix[r])

# print()

# for r in range(h):
#     print(*verticalPlacementPrefix[r])


q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]


def query(prefix, r1, c1, r2, c2):
    ans = prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1]

    return ans

for r1, c1, r2, c2 in queries:
    horizontal = query(horzontalPlacementPrefix, r1, c1, r2, c2-1)
    vertical = query(verticalPlacementPrefix, r1, c1, r2-1, c2)

    ans = horizontal + vertical

    print(ans)