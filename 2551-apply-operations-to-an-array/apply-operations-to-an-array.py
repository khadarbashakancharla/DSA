class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = nums[i] * 2, 0
        j = 0
        for k in range(len(nums)):
            if nums[k] !=0:
                nums[k], nums[j] = nums[j], nums[k]
                j = j+ 1
        return nums        