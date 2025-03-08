class Solution:
    #Zigzag Conversion
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        pat = [''] *numRows
        step = 0
        index = 0
        for ele in s:
            pat[index] += ele
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step  
        return (''.join(pat))          
        