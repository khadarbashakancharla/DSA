class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        p = ""
        for i in range(len(first)):
            if first[i] != last[i]:
                return p
            else:
                p += first[i]
        return p        
                


        