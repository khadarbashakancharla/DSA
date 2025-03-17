class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        unic_nums = set(nums)
        for ele in unic_nums:
            cnt = nums.count(ele)
            if cnt%2 != 0:
                return False
        return True        
        