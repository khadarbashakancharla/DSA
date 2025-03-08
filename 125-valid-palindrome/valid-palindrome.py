class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_string = ""
        for ele in s:
            if ele.isalpha() or ele.isdigit():
                modified_string += ele.lower()
        if modified_string == modified_string[::-1]:
            return True
        return False            