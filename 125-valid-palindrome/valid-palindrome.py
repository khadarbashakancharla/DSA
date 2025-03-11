class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for ele in s:
            if ele.isalpha() or ele.isdigit():
                new_str += ele.lower()
        if new_str == new_str[::-1]:
            return True
        return False            
