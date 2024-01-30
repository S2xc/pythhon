class Solution:
    def plusOne(self, digits):
        self.digits = digits
        self.digits = list(map(str, self.digits))
        
        self.j = ''.join(self.digits)
        self.j = int(self.j)
        self.j+=1
        self.j = str(self.j)
        
        return (list(map(int, self.j)))