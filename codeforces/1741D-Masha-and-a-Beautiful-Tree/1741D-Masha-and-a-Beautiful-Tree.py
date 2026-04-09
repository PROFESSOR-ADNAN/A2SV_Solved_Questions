# leaves = []
# def helper(node):
#     nonlocal leaves
#     if not node.left and not node.right:
#         leaves.append(node.val)
#         return

#     helper(node.left)
#     helper(node.right)


def solve(m, perm):
    operation = 0
    def merget_sort(left, right):
        nonlocal operation
        if left + 1 >= right:
            if perm[left] > perm[right]:
                perm[left], perm[right] = perm[right], perm[left]
                operation += 1
            return perm[left:right+1]
        
        mid = left + (right - left) // 2
        leftSide = merget_sort(left, mid)
        rightSide = merget_sort(mid+1, right)

        if leftSide[0] > rightSide[0]:
            operation += 1
            return rightSide + leftSide
        else:
            return leftSide + rightSide

    final = merget_sort(0, len(perm)-1)

    if final == sorted(perm):
        print(operation)
    else:
        print(-1)



for _ in range(int(input())):
    m = int(input())
    perm = list(map(int, input().split()))

    solve(m, perm)