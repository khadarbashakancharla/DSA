class Solution:
    def hammingWeight(self, n: int) -> int:
        s = ''
        while n > 0:
            s = str(n%2)+s
            n = n//2
        s = list(s)
        return s.count('1')
            
        

        