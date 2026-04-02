class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # total_weight = sum(weights)

        # def isPoss(capacity):
        #     curr_reqired_day = total_weight // capacity
        #     return curr_reqired_day <= days

        # left, right = max(weights), total_weight
        # while left <= right:
        #     mid = (left + right) // 2
        #     if isPoss(mid):
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        # return left

        # total = sum(weights)

        # def isValid(val):
        #     d = 0
        #     curr = 0
        #     for weight in weights:
        #         curr += weight
        #         if curr == val:
        #             d += 1
        #             curr = 0
        #         elif curr > val:
        #             curr = weight
        #             d += 1

        #     if curr > 0:
        #         d += 1
            
        #     return d <= days

        # low, high = max(weights), total

        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         high = mid - 1
        #     else:
        #         low = mid + 1
            
        # return low


        def isValid(val):
            load = 0
            d = 1
            for weight in weights:
                if load + weight > val:
                    d += 1
                    load = weight
                else:
                    load += weight

            return d <= days


        low, high = max(weights), sum(weights)
        while low <= high:
            mid = low + (high - low) // 2
            if isValid(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low