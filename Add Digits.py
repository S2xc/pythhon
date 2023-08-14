class Solution:
    def addDigits(self, num: int) -> int:
        self.num = num
        self.lyt = 2

        while self.lyt > 1:
            self.uio = sum(map(int, list(str(self.num))))
            self.lyt = len(list(str(self.uio)))
            self.num = self.uio

        return self.uio