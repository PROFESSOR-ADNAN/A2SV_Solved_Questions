# from collections import Counter


# def helper(s, t):
#     countS = Counter(s)
#     countT = Counter(t)

#     for key, value in countS.items():
#         if key not in countT or value > countT[key]:
#             return "Impossible"
        
#     temp = []

#     for k in countT.keys():
#         if k not in countS:
#             temp.append(k)

    # temp.sort()
    # print(temp)
    # ans = []
    # i, j = 0, 0

    # while i < len(temp) and j < len(s):
    #     if temp[i] <= s[j]:
    #         ans.append(temp[i])
    #         i += 1
    #     else:
    #         ans.append(s[j])
    #         j += 1

    # if i < len(temp): ans.extend(temp)
    # elif j < len(s): ans.extend(s)

    # return "".join(ans)

# for _ in range(int(input())):
#     s = input()
#     t = input()
#     print(helper(s, t))


from collections import Counter


def helper(s, t):
    countS = Counter(s)
    countT = Counter(t)

    for key, value in countS.items():
        if key not in countT or value > countT[key]:
            return "Impossible"
     
    for key, value in countT.items():
        if key in countS:
            countT[key] -= countS[key]
    temp = []

    for key, value in countT.items():
        if value > 0:
            temp.append(key * value)

    temp.sort()

    ans = []
    i, j = 0, 0

    while i < len(temp) and j < len(s):
        if temp[i] < s[j]:
            ans.append(temp[i])
            i += 1
        else:
            ans.append(s[j])
            j += 1

    if i < len(temp): ans.extend(temp[i:])
    elif j < len(s): ans.extend(s[j:])

    return "".join(ans)

for _ in range(int(input())):
    s = input()
    t = input()
    print(helper(s, t))
