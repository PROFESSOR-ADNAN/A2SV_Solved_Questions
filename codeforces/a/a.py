# #!/usr/bin/env pypy3
# from sys import stdin
# from collections import defaultdict
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
#     graph = defaultdict(list)
#     for _ in range(n-1):
#         u, v = mi()
#         graph[u].append(v)
#         graph[v].append(u)

#     visited = set()
#     def dfs(node, length):
#         nonlocal longest

#         visited.add(node)
#         for nei in graph[node]:
#             if nei not in visited:
#                 length += 1
#                 dfs(nei, length)
#                 print(length)
#                 longest = max(longest, length)

#     longest = 0
#     for i in range(1, n+1):
#         dfs(i, 0)

#     print(3 * longest)

# def main():
#     t = 1
#     # t = ii()
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()



# #!/usr/bin/env pypy3
# from sys import stdin
# from collections import defaultdict, deque
# input = stdin.readline

# def si():
#     return input().strip()

# def ii():
#     return int(input())

# def mi():
#     return map(int, input().split())

# def li():
#     return list(map(int, input().split()))

# def find_farthest(start, graph, n):
#     dist = [-1] * (n+1)
#     dist[start] = 0

#     q = deque([start])

#     while q:
#         curr = q.popleft()
#         for nei in graph[curr]:
#             if dist[nei] == -1:
#                 dist[nei] = dist[curr] + 1
#                 q.append(nei)

#     farthest_node = max(range(1, n+1), key = lambda x: dist[x])
#     return farthest_node, dist[farthest_node]

# def solve():
#     n = ii()
#     graph = defaultdict(list)
#     for _ in range(n-1):
#         u, v = mi()
#         graph[u].append(v)
#         graph[v].append(u)

#     farthest_node, _ = find_farthest(1, graph, n)
#     other_end, diameter = find_farthest(farthest_node, graph, n)

#     print(3 * diameter)


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

def si():
    return input().strip()

def ii():
    return int(input())

def mi():
    return map(int, input().split())

def li():
    return list(map(int, input().split()))

def find_farthest(start, graph, n):
    dist = [-1] * (n+1)
    dist[start] = 0

    q = deque([start])

    while q:
        curr = q.popleft()
        for nei in graph[curr]:
            if dist[nei] == -1:
                dist[nei] = dist[curr] + 1
                q.append(nei)

    farthest_node = max(range(1, n+1), key=lambda x: dist[x])
    return farthest_node, dist[farthest_node]

def solve():
    n = ii()
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = mi()
        graph[u].append(v)
        graph[v].append(u)

    farthest_node, _ = find_farthest(1, graph, n)
    other_end, diameter = find_farthest(farthest_node, graph, n)

    print(3 * diameter)


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()