class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            'I' : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, 'M' : 1000
        }

        t = 0
        p = 0
        for ele in reversed(s):
            value = sym[ele]
            if value < p:
                t -= value
            else:
                t += value 
                p = value
        return t           