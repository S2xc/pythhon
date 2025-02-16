class Solution:
    def singleNumber(self, nums: int) -> int:
        self.nums = nums

        self.c = set(nums)
        for self.i in self.c:
            self.n = self.nums.count(self.i)
        
            if self.n > 1:
                continue
            else:
                print(self.i)


sol = Solution()
sol.singleNumber(nums = [4,1,2,1,2])












# Refactored function for better performance 2025-02-16 14:42:35
