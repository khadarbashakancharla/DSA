class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for ele in nums:
            if ele in duplicates:
                return True
            else:
                duplicates.add(ele)
        return False            

