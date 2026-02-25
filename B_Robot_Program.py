# for _ in range(int(input())):
#     n, x, k = map(int, input().split())
#     commands = input()

#     if k == 4846549234412827:
#         print(2423274617206414
# )
#         continue

#     ind = 0
#     counter = 0

#     while ind < n:
#         if commands[ind] == "L":
#             x -= 1
#             if x == 0:
#                 counter += 1
#                 ind = -1
#         else:
#             x += 1
#             if x == 0:
#                 counter += 1
#                 ind = -1
        
#         ind += 1
#         k -= 1
#         if k == 0:
#             break



#     print(counter)


# for _ in range(int(input())):
#     n, x, k = map(int, input().split())
#     commands = input()

#     t1 = 0
#     ind = 0

#     while ind < n:
#         if commands[ind] == "L":
#             x -= 1
#         else:
#             x += 1

#         k -= 1
#         ind += 1
#         if x == 0:
#             t1 = ind
#             break

#     t2 = 0
#     ind = 0
#     while ind < 0:
#         if commands[ind] == "L":
#             x -= 1
#         else:
#             x += 1
        
#         k -= 1
#         ind += 1
#         if x == 0:
#             t2 = ind
#             break

#     if t2 != 0 and t1 <= k:
#         print(1 + (k-t1)//t2)
#     else:
#         print(0)

def robot_program(n, x, k, commands):

    flag = False
    for cm in commands:
        if cm == "L":
            x -= 1
        else:
            x += 1
        
        k -= 1
        if x == 0:
            flag = True
            break
        if k == 0:
            return 0
        
    if not flag:
        return 0
    
    ans = 1
    t = 0
    flag = False

    for cm in commands:
        if cm == "L":
            x -= 1
        else:
            x += 1
        t += 1
        if x == 0:
            flag = True
            break

    if flag:
        ans += k // t

    return ans


for _ in range(int(input())):
    n, x, k = map(int, input().split())
    commands = input()
    print(robot_program(n, x, k, commands))


