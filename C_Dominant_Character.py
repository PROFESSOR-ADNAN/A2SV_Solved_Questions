# for _ in range(int(input())):
#     n = int(input())
#     string = input()

#     min_len = float("inf")

#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             curr = string[i:j+1]
#             cntA, cntB, cntC = curr.count("a"), curr.count("b"), curr.count("c")

#             if j-i+1 >= 2 and cntA > cntB and cntA > cntC:
#                 min_len = min(min_len, j-i+1)

#     if min_len != float("inf"): print(min_len)
#     else: print(-1)

# for _ in range(int(input())):
#     n = int(input())
#     string = input()

#     min_len = float("inf")
#     l, r = 0, 0

#     while r < len(string):
#         curr = string[l:r+1]
#         cntA, cntB, cntC = curr.count("a"), curr.count("b"), curr.count("c")
        
#         while l <= r and (cntA <= cntB or cntA <= cntC):
#             l += 1
#             curr = string[l:r+1]
#             cntA, cntB, cntC = curr.count("a"), curr.count("b"), curr.count("c")
            
#         if (r-l+1) >= 2:
#             min_len = min(min_len, r-l+1)

#         r += 1

#     if min_len != float("inf"):
#         print(min_len)
#     else:
#         print(-1)





# for _ in range(int(input())):
#     n = int(input())
#     string = input()

#     min_len = float("inf")
#     l, r = 0, 0

#     while r < len(string):
#         curr = string[l:r+1]
#         cntA, cntB, cntC = curr.count("a"), curr.count("b"), curr.count("c")

#         print(curr)
#         print(cntA, cntB, cntC) 

#         while r < len(string) and (cntA <= cntB or cntA <= cntC) and (r-l+1) >= 2:
#             print("inside1", curr)
#             print("inside1", cntA, cntB, cntC)

#             r += 1
#             curr = string[l:r+1]
#             cntA, cntB, cntC = curr.count("a"), curr.count("b"), curr.count("c")


#         if r == len(string):
#             break

#         while (r-l+1) >= 2:
#             min_len = min(min_len, r-l+1)
#             l += 1
#             curr = string[l:r+1]
#             cntA, cntB, cntC = curr.count("a"), curr.count("b"), curr.count("c")


#             print("inside2", curr)
#             print("insdie2", cntA, cntB, cntC)


#         r += 1

#     if min_len != float("inf"):
#         print(min_len)
#     else:
#         print(-1)

# from collections import defaultdict 

# for _ in range(int(input())):
#     n = int(input())
#     s = input()

#     count = {"a": 0, "b": 0, "c": 0}
#     min_len = float("inf")
#     l = 0

#     for r in range(len(s)):
#         count[s[r]] += 1
#         while count["a"] > count["b"] and count["a"] > count["c"] and (r-l+1) >= 2:

#             if (r-l+1) >= 2:
#                 min_len = min(min_len, r-l+1)

#             count[s[l]] -= 1
#             l += 1
    
#     print(min_len if min_len != float("inf") else -1)


# for _ in range(int(input())):
#     n = int(input())
#     s = input()

#     ans = -1

#     for length in range(2, 8):
#         if ans != -1: break
#         for i in range(n-length+1):
#             subString = s[i:i+length]
#             if(subString.count("a") > subString.count("b") and subString.count("a") > subString.count("c")):
#                 ans = length

#     print(ans)


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 8

    for i in range(len(s)):
        if s[i] == "a":

            for j in range(i+1, min(i+7, n)):
                sub = s[i:j+1]
                cntA, cntB, cntC = sub.count("a"), sub.count("b"), sub.count("c")

                if cntA > cntB and cntA > cntC:
                    ans = min(ans, j-i+1)

                    if ans == 2: break

    print(ans if ans < 8 else -1)