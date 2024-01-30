class Solution:
    def singleNumber(self, nums: int) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        print(res)
    

sol = Solution()
sol.singleNumber(nums = [4,1,2,1,2])