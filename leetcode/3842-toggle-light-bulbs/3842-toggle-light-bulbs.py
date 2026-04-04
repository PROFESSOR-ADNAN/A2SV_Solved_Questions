class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        count = Counter(bulbs)

        ans = []
        for key, value in count.items():
            if value % 2:
                ans.append(key)
        
        return sorted(ans)