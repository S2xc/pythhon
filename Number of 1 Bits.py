class Solution:
    def hammingWeight(self, n: int) -> int:
        self.n = n
        self.n = list(str(self.n))
        print(self.n.count('1'))
    

sol = Solution()
sol.hammingWeight(n = int(input()))