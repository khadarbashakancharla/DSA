class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        previous = 0
        for digit in reversed(s):
            if sym[digit] < previous:
                total -= sym[digit]
            else:    
                total += sym[digit]
                previous = sym[digit]
        return total    
                
