class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # max_len = 0
        # n = len(nums)
        # nums.sort()

        # if not nums:
        #     return 0

        # l = 0
        # r = 1
        # duplicate = 0

        # while r < n:
        #     if nums[r] == nums[r-1] + 1:
        #         r += 1
        #     elif nums[r] == nums[r-1]:
        #         duplicate += 1
        #         r += 1
        #     else:
        #         print(r, duplicate)
        #         max_len = max(max_len, r-l-duplicate)
                # l = r
        #         r += 1
        #         duplicate = 0

        # max_len = max(max_len, r-l-duplicate)
        # return max_len

        # if not nums:
        #     return 0

        # max_len = 0
        # n = len(nums)

        # sett = set(nums)

        # for i in range(n):
        #     curr = nums[i]
        #     longest = 0
        #     while curr in sett:
        #         curr -= 1
        #         longest += 1

        #     max_len = max(max_len, longest)

        # return max_len



        # if not nums:
        #     return 0

        # max_len = 0
        # n = len(nums)

        # sett = set(nums)

        # for i in range(n):
        #     curr = nums[i]
        #     if curr - 1 in sett:
        #         continue
        #     longest = 0
        #     while curr in sett:
        #         curr += 1
        #         longest += 1

        #     max_len = max(max_len, longest)

        # return max_len

        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in num_set:
                length = 0
                while (n+length) in num_set:
                    length += 1

                longest = max(longest, length)

        return longest