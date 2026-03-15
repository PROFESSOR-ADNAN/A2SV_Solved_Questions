# def bubble_sort(arr, operationCount, operationType, type):
#     n = len(arr)
#     for i in range(len(arr)):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#                 operationType.append([type, j+1])
#                 operationCount += 1

#     return operationCount

# def solve(n, a, b):
#     operationCount = 0
#     operationType = []
#     tempa = a.copy()
#     tempb = b.copy()

#     tempa.sort()
#     tempb.sort()

#     flag = True
#     for i in range(len(tempa)):
#         if tempa[i] > tempb[i]:
#             flag = False

#     if flag:
#         operationCount = bubble_sort(a, operationCount, operationType, 1)
#         operationCount = bubble_sort(b, operationCount, operationType, 2)
#     else:
#         for i in range(len(a)):
#             2, 4
#             1, 3

#             if a[i] <= n and b[i] <= n:
#                 if a[i] > b[i]:
#                     a[i], b[i] = b[i], a[i]    

#                     operationType.append([3, i+1])
#                     operationCount += 1
#             if a[i] > n:
#                 a[i], b[i] = b[i], a[i]

#                 operationType.append([3, i+1])
#                 operationCount += 1

#         operationCount = bubble_sort(a, operationCount, operationType, 1)
#         operationCount = bubble_sort(b, operationCount, operationType, 2)

#     print(operationCount)
#     for type, index in operationType:
#         print(type, index)

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
    
#     solve(n, a, b)









def bubble_sort(arr, operationCount, operationType, type):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                operationType.append([type, j+1])
                operationCount += 1

    return operationCount

def solve(n, a, b):
    operationCount = 0
    operationType = []

    operationCount = bubble_sort(a, operationCount, operationType, 1)
    operationCount = bubble_sort(b, operationCount, operationType, 2)

    for i in range(len(a)):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]

            operationType.append([3, i+1])
            operationCount += 1

    print(operationCount)
    for type, index in operationType:
        print(type, index)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    solve(n, a, b)