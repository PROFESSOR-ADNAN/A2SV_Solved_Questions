def helper(s):
    finalS = 0
    for op in s:
        if op == "+":
            finalS += 1
        else:
            finalS -= 1

    return finalS

def solve(s1, s2):
    finalS1 = helper(s1)
    allPoss = []
    path = []

    def backtrack(i):
        if len(path) == len(s2):
            allPoss.append(path[:])
            return
        if i >= len(s2):
            return

        curr = s2[i]
        if curr != "?":
            path.append(curr)
            backtrack(i+1)
            path.pop()
        else:
            path.append("+")
            backtrack(i+1)
            path.pop()

            path.append("-")
            backtrack(i+1)
            path.pop()

    backtrack(0)

    total = len(allPoss)
    correntPosition = 0
    for poss in allPoss:
        curr = "".join(poss)
        res = helper(curr)
        if res == finalS1:
            correntPosition += 1

    print(float(correntPosition/total))


s1 = input()
s2 = input()

solve(s1, s2)