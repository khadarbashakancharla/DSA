class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        for ele in nums:
            current_sum += ele
            max_sum = max(max_sum,current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum        