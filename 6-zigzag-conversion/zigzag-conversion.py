class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        index = 0
        step = 1
        rows = ['']*numRows
        for ele in s:
            rows[index] += ele
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1    
            index += step   
        return (''.join(rows))         

        