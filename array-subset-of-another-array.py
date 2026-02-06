from collections import Counter
#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        countB = Counter(b)
        countA = Counter(a)
        
        for key, value in countB.items():
            if countA[key] < value:
                return False
                
        return True