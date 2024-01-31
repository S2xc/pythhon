class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

sol = Solution()
print(sol.hammingWeight(11111111111111111111111111111101))



