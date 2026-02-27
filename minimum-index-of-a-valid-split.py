class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
#         # def helper(nums):
#         #     count = Counter(nums)

#         #     dominant = 0
#         #     cnt = 0
#         #     for key, value in count.items():
#         #         if value > cnt:
#         #             dominant = key
#         #             cnt = value
#         #             flag = True
#         #         elif value == cnt:
#         #             flag = False

#         #     return [flag, dominant, cnt] if flag else [flag]


#         # dominant, cnt = helper(nums)
#         # occurrence = 0
#         # for i in range(len(nums)):
#         #     num = nums[i]
#         #     if num == dominant:
#         #         occurrence += 1
#         #         f1, d1, c1, f2, d2, c2 = helper(nums[:i+1]), helper(nums[i+1:])
#         #         if f1 and f2:
                    
#         # def helper(count):
#         #     dominant = -1
#         #     max_count = 0
#         #     for key, value in count.items():
#         #         if value > max_count:
#         #             dominant = key
#         #             max_count = value
#         #         elif value == max_count:
#         #             dominant = -1

#         #     return [dominant, max_count]

#         def helper(nums, count):
#             maxHeap = [-1 * nums[i] for i in range(len(nums))]
#             heapq.heapify(maxHeap)
            
#             dominant = -1 * heapq.heappop(maxHeap)
#             cnt = count[dominant]

#             return [dominant, cnt]


#         n = len(nums)
#         first = Counter()
#         second = Counter(nums)
#         [dominant, cnt] = helper(nums, second)

#         for i in range(len(nums)-1):
#             first[nums[i]] += 1
#             second[nums[i]] -= 1
#             if second[nums[i]] == 0:
#                 del second[nums[i]]

#             d1, c1 = helper(nums[:i+1], first)
#             d2, c2 = helper(nums[i+1:], second)

#             if d1 != dominant or d2 != dominant:
#                 continue

#             if c1 * 2 > i+1 and c2 * 2 > (n-i-1):
#                 return i

#         return -1

        count = Counter(nums)
        x = -1
        f = 0
        for key, value in count.items():
            if value > f:
                x = key
                f = value
        f1 = 0
        f2 = f
        n = len(nums)

        for i in range(len(nums)-1):
            if nums[i] == x:
                f2 -= 1
                f1 += 1

            if f1 * 2 > (i+1) and f2 * 2 > (n-i-1):
                return i

        return -1