class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for ele in nums:
            subsets += [current+[ele] for current in subsets]
        return subsets    

        