class Solution:
    def addDigits(self, num: int) -> int:
        self.num = num
        self.lyt = 2

        while self.lyt > 1:
            self.gh = sum(map(int, list(str(self.num))))
            self.lyt = len(list(str(self.gh)))
            self.num = self.gh

        return self.gh