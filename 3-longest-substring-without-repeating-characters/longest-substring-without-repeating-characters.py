class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        sub = set()
        l = 0
        while right < len(s):
            if s[right] not in sub:
                sub.add(s[right])
                l = max(len(sub),l)
                right +=1
            else:
                sub.remove(s[left])
                left += 1
        return l            



        