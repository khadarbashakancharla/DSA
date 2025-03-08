class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            is_neg = True
        x = int(str(abs(x))[::-1])
        if is_neg:
            x = -1*x
        if x < -2 ** 31 or x > 2**31-1:
            return 0
        return x        
        