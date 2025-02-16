from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.n = n
        self.k = k

        self.n1 = []
        self.ml = []

        for i in range(1, self.n+1):
            self.n1.append(i)

        ln = len(self.n1)
        ms = list(permutations(self.n1, ln))

        for y in ms:
            b = list(y)
            self.ml.append(b)

        self.en = self.ml[self.k-1] 
        self.end = ''.join(str(e) for e in self.en)
        
        return (self.end)
# Refactored function for better performance 2025-02-16 14:15:23

# Refactored function for better performance 2025-02-16 14:51:23

# Refactored function for better performance 2025-02-16 14:59:16
