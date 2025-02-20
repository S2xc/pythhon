from itertools import permutations
x = [0]
ml = []

l = len(x)

# Refactored function for better performance - 2025-02-20 18:43:08
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

# Refactored function for better performance - 2025-02-20 18:43:02
                num =[(i),(y),(o)]
                 
                j.append(num)


# Refactored function for better performance - 2025-02-20 18:51:57
print(j)'''

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:51:36

# Refactored function for better performance 2025-02-16 14:52:09

# Refactored function for better performance 2025-02-16 14:52:22

# Refactored function for better performance 2025-02-16 14:59:00

# Refactored function for better performance 2025-02-16 14:59:02

# Refactored function for better performance 2025-02-16 14:59:28

# Refactored function for better performance 2025-02-16 14:59:30

# Refactored function for better performance 2025-02-16 15:02:02

# Refactored function for better performance 2025-02-16 15:05:57

# Refactored function for better performance 2025-02-16 15:11:20
