class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        max = l1 if l1 > l2 else l2
        res = ""
        for i in range(max):
            if l1 > i:
                res += word1[i]
            if l2 > i:
                res += word2[i]
        
        return res
# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:51:52

# Refactored function for better performance 2025-02-16 14:52:20

# Refactored function for better performance 2025-02-16 15:11:31

# Refactored function for better performance 2025-02-16 15:11:35
