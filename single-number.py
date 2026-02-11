class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count_nums = Counter(nums)
        # for key, value in count_nums.items():
        #     if value == 1:
        #         return key

        for ind, num in enumerate(nums):
            if num not in (nums[:ind]+nums[ind+1:]):
                return num
        
