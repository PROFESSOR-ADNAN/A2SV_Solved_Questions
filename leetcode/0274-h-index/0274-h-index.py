class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort()
        # n = len(citations)
        # for i in range(n):
        #     if citations[i] >= n - i:
        #         return n - i

        # return 0

        # citations.sort(reverse = True)

        # def isValid(ind):
        #     return citations[ind-1] >= ind

        # low, high = 1, len(citations)
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if isValid(mid):
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        
        # return high


        citations.sort()
        n = len(citations)

        for h in range(n, 0, -1):
            idx = bisect.bisect_left(citations, h)
            if n - idx >= h:
                return h

        return 0