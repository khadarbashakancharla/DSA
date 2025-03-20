class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        left = 0 
        right = 0
        len_of_str = 0
        while right < len(s):
            if s[right] not in sub_string:
                sub_string.add(s[right])
                len_of_str = max(len(sub_string),len_of_str)
                right += 1
            else:
                sub_string.remove(s[left])
                left += 1
        return len_of_str                      

        