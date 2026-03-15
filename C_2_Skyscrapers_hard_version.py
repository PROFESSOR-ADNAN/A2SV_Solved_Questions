# def solve(n, m):
#     ind = 1
#     while ind < n:
#         if m[ind-1] <= m[ind]:
#             ind += 1
#         else:
#             break
    
#     ans = []

#     for i in range(1, ind):
#         if m[i-1] <= m[i]:
#             ans.append(m[i-1])
#         else:
#             ans.append(m[i])

#     ans.append(m[ind-1])

#     for i in range(ind, n):
#         if m[i-1] >= m[i]:
#             ans.append(m[i])
#         else:
#             ans.append(m[i-1])

#     print(*ans)


# n = int(input())
# m = list(map(int, input().split()))

# solve(n, m)


# def solve(n, m):
#     stack = []
#     ind = 1
    
#     while ind < n and m[ind-1] <= m[ind]:
#         stack.append(m[ind-1])
#         ind += 1

#     stack.append(m[ind-1])

#     while ind < n:
#         if m[ind-1] >= m[ind]:
#             stack.append(m[ind])
#         else:
#             stack.append(m[ind-1])
        
#         ind += 1

#     print(*stack)


# n = int(input())
# m = list(map(int, input().split()))

# solve(n, m)



# def solve(n, m):
#     max_ = max(m)

#     stack = []
#     ind = 1
    
#     while ind < n and m[ind-1] != max_:
#         if m[ind-1] <= m[ind]:
#             stack.append(m[ind-1])
#         else:
#             stack.append(m[ind])
#         ind += 1

#     stack.append(m[ind-1])

#     while ind < n:
#         if m[ind-1] >= m[ind]:
#             stack.append(m[ind])
#         else:
#             stack.append(m[ind-1])
        
#         ind += 1

#     print(*stack)


# n = int(input())
# m = list(map(int, input().split()))

# solve(n, m)




from collections import Counter, defaultdict, deque
from cmath import inf
from math import ceil


def iinput(): return int(input())
def sinput(): return input()
def iarray(): return list(map(int, input().split()))
def imatrix(rows): return [list(map(int,input().split())) for _ in range(rows)]
def smatrix(rows): return [input() for _ in range(rows)]
def mapinput(): return map(int, input().split())

n = iinput()
heights = iarray()

#left maximum side

left_peak = [0] * n
running_sum = 0
stack = []

for i in range(n): # considering every element as a peak calculate left peak
    while stack and heights[stack[-1]] > heights[i]:
        prev_idx = stack.pop()
        last_idx = stack[-1] if stack else -1
        running_sum -= (prev_idx - last_idx) * heights[prev_idx]
    
    last_idx = stack[-1] if stack else -1
    running_sum += (i - last_idx) * heights[i]
    left_peak[i] = running_sum
    stack.append(i)


right_peak = [0] * n
running_sum = 0
stack = []

for i in range(n-1,-1,-1): # considering every element as a peak calculate right peak
    while stack and heights[stack[-1]] > heights[i]:
        prev_idx = stack.pop()
        last_idx = stack[-1] if stack else -1
        running_sum -= (last_idx - prev_idx) * heights[prev_idx]
    
    last_idx = stack[-1] if stack else -1
    running_sum += (last_idx - i) * heights[i]
    right_peak[i] = running_sum
    stack.append(i)

best = 0
_max = -1


for i in range(n):
    total = left_peak[i] + right_peak[i] - heights[i]
    if total > _max:
        best = i
        _max = total

res = [0] * n
res[best] = heights[best]

#left
for i in range(best-1, -1, -1):
    res[i] = min(heights[i], res[i+1])
#right
for i in range(best+1, n):
    res[i] = min(heights[i], res[i-1])
print(*res)
