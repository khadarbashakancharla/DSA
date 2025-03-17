import collections 
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_of_digits = collections.Counter(nums)
        for count in count_of_digits.values():
            if count % 2 != 0:
                return False
        return True        
              
        