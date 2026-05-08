# #!/usr/bin/env pypy3
# from sys import stdin
# from collections import defaultdict
# input = stdin.readline

# def s_i():
#     return input().strip()

# def ii():
#     return int(input())

# def mi():
#     return map(int, input().split())

# def li():
#     return list(map(int, input().split()))

# def isThereCircle(graph, nodes):
#     print(graph, nodes)
#     white, gray, black = 0, 1, 2
#     color = {node:white for node in nodes}

#     def dfs(node):
#         color[node] = gray
#         for nei in graph[node]:
#             if color[nei] == gray: return True
#             if color[nei] == white: 
#                 if dfs(nei): return True

#         color[node] = black

# def solve():
#     n = ii()
#     names = [s_i() for _ in range(n)]

#     graph = defaultdict(list)
#     nodes = set()
#     for i in range(1, n):
#         s = names[i-1]
#         t = names[i]

#         ind = 0
#         while ind < len(s):
#             if ind >= len(t):
#                 print(Impossible)
#                 return

#             if s[ind] != t[ind]:
#                 si = s[ind]
#                 ti = t[ind]
#                 break
#             ind += 1
#         else:
#             continue

#         graph[si].append(ti)
#         nodes.add(si)
#         nodes.add(ti)

#     if isThereCircle(graph, nodes):
#         print(Impossible)
#         return

#     print("nocycle")


# def main():
#     t = 1
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()


# #!/usr/bin/env pypy3
# from sys import stdin
# from collections import defaultdict
# input = stdin.readline

# def s_i():
#     return input().strip()

# def ii():
#     return int(input())

# def mi():
#     return map(int, input().split())

# def li():
#     return list(map(int, input().split()))
    
# def solve():
#     n = ii()
#     names = [s_i() for _ in range(n)]

#     graph = defaultdict(list)
#     for i in range(n-1):
#         s, t = names[i], names[i+1]

#         minLen = min(len(s), len(t))
#         if s[:minLen] == t[:minLen] and len(s) > len(t):
#             print(Impossible)
#             return

#         ind = 0
#         while ind < len(s) and s[ind] == t[ind]:
#             ind += 1

#         graph[s[ind]].append(t[ind])

#     white, gray, black = 0, 1, 2
#     color = {chr(ord("a") + i):white for i in range(26)}
    
#     def dfs(node):
#         color[node] = gray
#         for nei in graph[node]:
#             if color[nei] == gray: return True
#             if color[nei] == white: 
#                 if dfs(nei):
#                     return True

#         color[node] = black
#         return False

#     for key in graph.keys():
#         if dfs(key):
#             print(Impossible)
#             return

#     print("nocyle")

# def main():
#     t = 1
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()



#!/usr/bin/env pypy3
from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

def s_i():
    return input().strip()

def ii():
    return int(input())

def mi():
    return map(int, input().split())

def li():
    return list(map(int, input().split()))
    
def solve():
    n = ii()
    names = [s_i() for _ in range(n)]

    graph = defaultdict(list)
    
    for i in range(n-1):
        s, t = names[i], names[i+1]

        minLen = min(len(s), len(t))
        diff_cond = False

        for j in range(minLen):
            if s[j] != t[j]:
                u, v = s[j], t[j]
                graph[u].append(v)
                diff_cond = True
                break

        if not diff_cond and len(s) > len(t):
            print("Impossible")
            return

    indegree = {chr(ord("a") + i): 0 for i in range(26)}

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([ch for ch in indegree if indegree[ch] == 0])
    answer = []

    while q:
        curr = q.popleft()
        answer.append(curr)
        for nei in graph[curr]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if len(answer) != 26:
        print("Impossible")
    else:
        print("".join(answer))

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()