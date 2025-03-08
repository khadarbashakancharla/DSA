class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1,rob2 = 0,0
        # for n in nums:
        #     temp = max(n+rob1,rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2    

        max_money = 0
        rob_money = 0
        for amount in nums:
            temp = max(amount+rob_money,max_money)
            rob_money = max_money
            max_money = temp
        return max_money    