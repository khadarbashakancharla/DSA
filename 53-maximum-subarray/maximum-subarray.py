class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        start = end = temp = 0
        sub = []
        for index,ele in enumerate(nums):
            current_sum += ele
            if max_sum < current_sum:
                max_sum = max(max_sum,current_sum)
                start = temp
                end = index
                sub = nums[start:end+1]
            if current_sum < 0:
                current_sum = 0
                temp = index
        return max_sum         
        





