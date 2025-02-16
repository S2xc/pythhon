from itertools import permutations
x = [0]
ml = []

l = len(x)
m = list(permutations(x,l))
for i in m:
    b=list(i)
    ml.append(b)
    
print(ml)


class Solution:
    def permute(self, nums: int) -> int:
        self.nums = nums

        self.ml = []
        self.l = len(self.nums)

        self.m = list(permutations(self.nums,self.l))
        for self.i in self.m:
            self.b = list(self.i)
            self.ml.append(self.b)

        return self.ml    



'''for i in nums:
    for y in nums:
        if i == y:
            continue
        for o in nums:
            if i == o or o == y:
                continue
            else:
                num =[(i),(y),(o)]
                 
                j.append(num)

print(j)'''

# Refactored function for better performance 2025-02-16 14:46:07
