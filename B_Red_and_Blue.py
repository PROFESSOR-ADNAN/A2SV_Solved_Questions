def solve(n, r, m, b):
    for i in range(1, n):
        r[i] += r[i-1]
    for i in range(1, m):
        b[i] += b[i-1]

    red_max = max(0, max(r))
    blue_max = max(0, max(b))

    print(red_max + blue_max)



for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    solve(n, r, m, b)