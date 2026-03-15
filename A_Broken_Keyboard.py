# from collections import defaultdict

# def solve(s):
#     unique_letter = set(s)
#     ans = set()
#     for ch in unique_letter:
#         consecutive_ch_cnt = defaultdict(int)
#         flag = True
#         i = 0
#         while i < len(s):
#             while i < len(s) and s[i] == ch:
#                 consecutive_ch_cnt[ch] += 1
#                 i += 1
#             if i == len(s):
#                 i -= 1
#             print(i)
#             if i < len(s) and s[i] != ch:
#                 if consecutive_ch_cnt[ch] % 2 != 0:
#                     ans.add(ch)     
#                     break
#                 consecutive_ch_cnt.clear()
#             i += 1
            
#     print(ans)




# for _ in range(int(input())):
#     solve(input())










# from collections import defaultdict

# def solve(s):
#     s += "A"
#     # zzaazA
#     consecutive_occurrence = defaultdict(list)

#     left, right = 0, 1
#     while right < len(s):
#         while right < len(s) and s[right] == s[left]:
#             right += 1

#         consecutive_occurrence[right-left].append(s[left])
        
#         left = right
#         right += 1

#     ans = set()
#     for key, value in consecutive_occurrence.items():
#         if key % 2 != 0:
#             for ch in value:
#                 ans.add(ch)
#     ans = [ch for ch in ans]
#     ans.sort()
#     res = "".join(ans)
#     print(res)


# for _ in range(int(input())):
#     solve(input())


def solve(s):
    n = len(s)
    ans = set()

    left = right = 0
    while left < n:
        left = right

        while right < n and s[right] == s[left]:
            right += 1

        if (right - left) % 2 != 0:
            ans.add(s[left])

        left = right


    print("".join(sorted(ans)))
        


for _ in range(int(input())):
    solve(input())
