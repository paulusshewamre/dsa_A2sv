#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        aCounter = {}
        bCounter = {}
        for num in a:
            aCounter[num] = aCounter.get(num, 0) + 1
        for num in b:
            bCounter[num] = bCounter.get(num, 0) + 1
        
        for key in bCounter:
            if key not in aCounter or bCounter[key] > aCounter[key]:
                return False
            
        return True
