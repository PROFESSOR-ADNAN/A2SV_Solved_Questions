import bisect

def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        b.sort()

        prev = -10**18
        possible = True

        for i in range(n):
            # Option 1: keep a[i]
            best = float('inf')
            if a[i] >= prev:
                best = a[i]

            # Option 2: transform
            target = prev + a[i]
            idx = bisect.bisect_left(b, target)

            if idx < m:
                transformed = b[idx] - a[i]
                best = min(best, transformed)

            if best == float('inf'):
                possible = False
                break

            prev = best

        print("YES" if possible else "NO")

solve()