class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # if x == int(str(x)[::-1]):
        #     return True
        # return False        
        if x<0:
            return False

        temp = x
        reversed_x = 0
        while x!=0:
            rem = x%10
            reversed_x = reversed_x * 10 + rem
            x = x // 10
        if temp == reversed_x:
            return True
        return False            