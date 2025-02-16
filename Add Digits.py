class Solution:
    def addDigits(self, num: int) -> int:
        self.num = num
        self.lyt = 2

        while self.lyt > 1:
            self.uio = sum(map(int, list(str(self.num))))
            self.lyt = len(list(str(self.uio)))
            self.num = self.uio

        return self.uio
# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:51:25

# Refactored function for better performance 2025-02-16 14:51:36
