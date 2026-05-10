# # #!/usr/bin/env pypy3
# # from sys import stdin
# # from collections import defaultdict
# # input = stdin.readline

# # def si():
# #     return input().strip()

# # def ii():
# #     return int(input())

# # def mi():
# #     return map(int, input().split())

# # def li():
# #     return list(map(int, input().split()))

# # def solve():
# #     n = ii()
# #     grid = [si() for _ in range(n)]

# #     con = defaultdict(list)

# #     for i in range(n):
# #         cnt = grid[i].count("1")    
# #         con[int(cnt)].append(i+1)

# #     ans = []
# #     for i in range(n):
# #         curr = con[i]
# #         curr.reverse()
# #         ans.extend(curr)

# #     print(*ans)

# # def main():
# #     t = ii()
# #     for _ in range(t):
# #         solve()

# # if __name__ == "__main__":
# #     main()


# #!/usr/bin/env pypy3
# from sys import stdin
# input = stdin.readline

# def si():
#     return input().strip()

# def ii():
#     return int(input())

# def mi():
#     return map(int, input().split())

# def li():
#     return list(map(int, input().split()))

# def solve():
#     n = ii()
#     graph = []
#     for _ in range(n):
#         curr = si()
#         graph.append(curr)
    
#     perm = [0] * n
#     for i in range(n):
#         curr = graph[i]
#         cnt = curr[i:].count("1")
#         idx = n - 1
#         while idx > 0:
#             if cnt == 0:
#                 break

#             if curr[idx] == 0:
#                 idx -= 1
#                 cnt -= 1
#             else:
#                 idx -= 1
                
#         while idx >= 0 and perm[idx] > 0:
#             idx -= 1
#         perm[idx] = i+1

#     print(*perm)
            

# def main():
#     t = ii()
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()






# #!/usr/bin/env pypy3
# from sys import stdin
# input = stdin.readline

# def si():
#     return input().strip()

# def ii():
#     return int(input())

# def mi():
#     return map(int, input().split())

# def li():
#     return list(map(int, input().split()))

# def solve():
#     n = ii()
#     grid = []
#     for _ in range(n):
#         curr = si()
#         grid.append(curr)

#     degree = []
#     for i in range(n):
#         degree.append(grid[i][i+1:].count("1"))

#     ans = [-1] * n
#     for i in range(n):
#         pos = n - degree[i] - 1
#         while ans[pos] != -1:
#             pos -= 1
#         ans[pos] = i+1

#     print(*ans)
    
# def main():
#     t = ii()
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()



# #!/usr/bin/env pypy3
# from sys import stdin
# input = stdin.readline

# def si():
#     return input().strip()

# def ii():
#     return int(input())

# def mi():
#     return map(int, input().split())

# def li():
#     return list(map(int, input().split()))

# def solve():
#     n = ii()
#     grid = []
#     for _ in range(n):
#         curr = si()
#         grid.append(curr)

#     ans = [-1] * n
#     for i in range(n):
#         cnt = 0
#         for j in range(i+1, n):
#             if grid[i][j] == "1": cnt += 1

#         for k in range(n-1, -1, -1):
#             if ans[k] == -1 and cnt == 0:
#                 ans[k] = i+1
#                 break
#             else:
#                 if ans[k] == -1: cnt -= 1

#     print(*ans)
    
# def main():
#     t = ii()
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()



#!/usr/bin/env pypy3
from sys import stdin
input = stdin.readline

def si():
    return input().strip()

def ii():
    return int(input())

def mi():
    return map(int, input().split())

def li():
    return list(map(int, input().split()))

def solve():
    n = ii()
    grid = []
    for _ in range(n):
        curr = si()
        grid.append(curr)


    perm = [-1] * n
    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if grid[i][j] == "1": cnt += 1
        
        for k in range(n-1, -1, -1):
            if perm[k] == -1 and cnt == 0:
                perm[k] = i+1
                break
            elif perm[k] == -1: cnt -= 1

    print(*perm)

def main():
    t = ii()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()