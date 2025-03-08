class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_ = 0
        sub_ = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    if l_ < len(sub):
                        l_ = len(sub)
                        sub_ = s[i:j+1] 
        return sub_                

        