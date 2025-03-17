class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        for ele in nums:
            cnt = nums.count(ele)
            if cnt%2 != 0:
                return False
        return True        
        