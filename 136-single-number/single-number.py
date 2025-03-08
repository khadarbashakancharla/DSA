class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for ele in nums:
            if nums.count(ele) == 1:
                count = ele
        return count        
                
        