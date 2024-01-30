class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        self.haystack = haystack
        self.needle = needle

        if self.needle in self.haystack:
            return (self.haystack.index(self.needle))
        else:
            return (-1)