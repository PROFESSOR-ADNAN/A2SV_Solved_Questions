# # def solve(brackets):
# #     longest = 0
# #     count = 0

# #     stack = []
# #     left = 0
# #     for right in range(len(brackets)):
# #         curr = brackets[right]
# #         if curr == "(":
# #             stack.append(curr)
# #         else:
# #             if stack:
# #                 stack.pop()
# #             else:
# #                 longest = max(longest, right - left)
# #                 count += 1
# #                 left = right + 1
# #                 stack.clear()

# #     if longest == 0:
# #         longest = max(longest, right - left + 1)
# #         count += 1


# #     print(longest, count)


# # brackets = input()
# # solve(brackets)


# def solve(brackets):
#     ans = []
#     temp = []
#     stack = []
    
#     for right in range(len(brackets)):
#         curr = brackets[right]
#         if curr == "(":
#             stack.append(curr)
#             temp.append(curr)
#         else:
#             if stack:
#                 stack.pop()
#                 temp.append(curr)
#             else:
#                 if temp:
#                     ans.append("".join(temp))
#                 stack = []
#                 temp = []

#     ans.append("".join(temp))

#     longest = 0
#     count = 0

#     for a in ans:
#         if len(a) % 2 == 0:
#             longest = max(longest, len(a))
#             count += 1

#     if count == 0:
#         count = 1

#     print(longest, count)


# brackets = input()
# solve(brackets)


def solve(brackets):
    mx = 0
    count = 0
    stack = [-1]

    for i in range(len(brackets)):
        curr = brackets[i]
        if curr == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                curr_len = i - stack[-1]
                if curr_len > mx:
                    mx = curr_len
                    count = 1
                elif curr_len == mx:
                    count += 1

    if mx == 0:
        print(0, 1)
    else:
        print(mx, count)


brackets = input()
solve(brackets)