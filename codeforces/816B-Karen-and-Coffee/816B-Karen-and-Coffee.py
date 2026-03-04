# def solve2(admissible, a, b):
#     count = 0
#     for val in range(a, b+1):
#         if val in admissible:
#             count += 1
#     return count


# def solve(n, k, q, recipes, questions):
#     mn = float("inf")
#     mx = 0

#     for x, y in recipes:
#         mn = min(mn, x, y)
#         mx = max(mx, x, y)

#     for a, b in questions:
#         mn = min(mn, a, b)
#         mx = max(mx, a, b)

#     prefix = [0] * (mx - mn + 1)

#     for x, y in recipes:
#         prefix[x-mn] += 1
#         if (y-mn+1) < len(prefix):
#             prefix[y-mn+1] -=  1

#     for i in range(1, len(prefix)):
#         prefix[i] += prefix[i-1]

#     # admissible = set()
#     # for i in range(len(prefix)):
#     #     if prefix[i] >= k:
#     #         admissible.add(i+mn)

#     # for a, b in questions:
#     #     print(solve2(admissible, a, b))

    
# n, k, q = map(int, input().split())
# recipes = []
# for _ in range(n):
#     recipes.append(list(map(int, input().split())))

# questions = []
# for _ in range(q):
#     questions.append(list(map(int, input().split())))

# solve(n, k, q, recipes, questions)




# def solve(k, recipes, questions):
#     # mn = float("inf")
#     # mx = float("-inf")

#     # for x, y in recipes:
#     #     mn = min(mn, x, y)
#     #     mx = max(mx, x, y)

#     # for a, b in questions:
#     #     mn = min(mn, a, b)
#     #     mx = max(mx, a, b)

    
#     prefix = [0] * 200001

#     for x, y in recipes:
#         prefix[x] += 1
#         if y+1 < 200000:
#             prefix[y+1] -= 1

#     for i in range(1, len(prefix)):
#         prefix[i] += prefix[i-1]

#     for i in range(len(prefix)):
#         if prefix[i] >= k:
#             prefix[i] = 1
#         else:
#             prefix[i] = 0

#     for i in range(1, len(prefix)):
#         prefix[i] += prefix[i-1]

#     for a, b in questions:
#         if a > 0:
#             print(prefix[b]-prefix[a-1])
#         else:
#             print(prefix[b])





# n, k, q = map(int, input().split())
# recipes = []
# for _ in range(n):
#     recipes.append(list(map(int, input().split())))

# questions = []
# for _ in range(q):
#     questions.append(list(map(int, input().split())))

# solve(k, recipes, questions)


def solve(k, recipes, questions):
    mn = float("inf")
    mx = float("-inf")

    for x, y in recipes:
        mn = min(mn, x, y)
        mx = max(mx, x, y)

    for a, b in questions:
        mn = min(mn, a, b)
        mx = max(mx, a, b)

    prefix = [0] * (mx-mn+1)

    for x, y in recipes:
        prefix[x-mn] += 1
        if y-mn+1 < len(prefix):
            prefix[y-mn+1] -= 1

    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]

    for i in range(len(prefix)):
        if prefix[i] >= k:
            prefix[i] = 1
        else:
            prefix[i] = 0

    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]

    for a, b in questions:
        if a-mn > 0:
            print(prefix[b-mn]-prefix[a-mn-1])
        else:
            print(prefix[b-mn])


n, k, q = map(int, input().split())
recipes = []
for _ in range(n):
    recipes.append(list(map(int, input().split())))

questions = []
for _ in range(q):
    questions.append(list(map(int, input().split())))

solve(k, recipes, questions)