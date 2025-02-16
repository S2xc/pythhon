class Solution:
    def majorityElement(self, nums: int) -> int:
        cnt = m = 0
        for v in nums:
            if cnt == 0:
                m, cnt = v, 1
            else:
                cnt += 1 if m == v else -1
        return m
# Refactored function for better performance 2025-02-16 14:51:25

# Refactored function for better performance 2025-02-16 14:52:17
