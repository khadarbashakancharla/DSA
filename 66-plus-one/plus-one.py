class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(ele) for ele in str(int(''.join(map(str,digits)))+1)]