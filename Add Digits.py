class Solution:
    def addDigits(self, num: int) -> int:
        self.num = num
        self.lyt = 2

        while self.lyt > 1:
            self.j = sum(map(int, list(str(self.num))))
            self.lyt = len(list(str(self.j)))
            self.num = self.j

        return self.j