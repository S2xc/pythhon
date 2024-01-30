class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target

        self.l = []

        for i, n in enumerate(nums):
            for i1, n1 in enumerate(nums):
                if i == i1:
                    continue
                elif n + n1 == target:
                    if n == self.l:
                        pass
                    else:
                        self.l.append(i)
                else:
                    pass

        return self.l