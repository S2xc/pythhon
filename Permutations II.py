from itertools import permutations
'''x = [0]
ml = []

l = len(x)
m = list(permutations(x,l))
for i in m:
    b=list(i)
    ml.append(b)
    
print(ml)'''


class Solution:
    def permuteUnique(self, nums: int) -> int:
        self.nums = nums

        self.ml = []

        self.ln = len(self.nums)
        self.m = list(permutations(self.nums, self.ln))
        
        for i in self.m:
            self.b=list(i)
            if self.b in self.ml:
                continue
            else:
                self.ml.append(self.b)
    
        print(self.ml)


sol = Solution()
sol.permuteUnique(nums = [1,2,3])



























