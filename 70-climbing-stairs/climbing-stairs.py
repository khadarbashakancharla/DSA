class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        nstairs = [0] * (n+1)
        nstairs[1] = 1
        nstairs[2] = 2
        for i in range(3,n+1):
            nstairs[i] = nstairs[i-1] + nstairs[i-2]
        return nstairs[n]        