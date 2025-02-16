
#больно и ...
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""





'''class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i2 = []

        for i in str2:
            i2.append(i)
            j = str(''.join(i2))

            if str1.find(str2) != -1:
                pass
            else:
                if len(list(j)) == 1:
                    j = ''
                    break

        temp = []
        for x in j: 
            if x not in temp: 
                temp.append(x) 

        ints_list = temp 

        return (str(''.join(ints_list)))'''
# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:51:21

# Refactored function for better performance 2025-02-16 14:51:58
