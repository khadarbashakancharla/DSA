class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #return [int(ele) for ele in str(int(''.join(map(str,digits)))+1)]
        s = ''.join(map(str,digits))
        num = int(s)
        num = num + 1
        num = str(num)
        return [int(ele) for ele in num]

