from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        # countA = {}
        # for num in a:
        #     countA[num] = countA.get(num, 0) + 1
        
        # countB = {}
        # for num in b:
        #     countB[num] = countB.get(num, 0) + 1
        
        # return countA == countB
        
        return Counter(a) == Counter(b)