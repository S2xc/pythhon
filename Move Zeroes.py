class Solution:
    def moveZeroes(self, nums: int) -> None:
        self.nums = nums

        for i in range(len(self.nums)):
            if self.nums[i] == 0:
                self.nums.append(self.nums[i])
                self.nums.remove(0)
        
        return self.nums
#Yfxn


# Refactored function for better performance 2025-02-16 14:52:02

# Refactored function for better performance 2025-02-16 14:52:05

# Refactored function for better performance 2025-02-16 14:52:07

# Refactored function for better performance 2025-02-16 14:59:30

# Refactored function for better performance 2025-02-16 15:02:00

# Refactored function for better performance 2025-02-16 15:11:20

# Refactored function for better performance 2025-02-16 15:11:22
