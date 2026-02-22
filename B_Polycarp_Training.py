# n = int(input())
# contests = list(map(int, input().split()))

# contests.sort()
# day = 0
# k = 0

# ind = 0
# while ind < len(contests):
#     day += 1
#     if contests[ind] < day:
#         while ind < len(contests) and contests[ind] < day:
#             ind += 1
#     else:
#         k += 1
#         ind += 1

# print(k)


n = int(input())
contests = list(map(int, input().split()))

print(len(set(contests)))