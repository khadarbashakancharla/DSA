class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index,ele in enumerate(nums):
            if ele == target:return index
        return -1                  
                