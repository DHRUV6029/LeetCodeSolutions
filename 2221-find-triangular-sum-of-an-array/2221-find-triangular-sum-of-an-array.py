class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newN = nums.copy()

        def GetNextSeries(nums):
            newNum= []
            for x in range(0 ,len(nums)-1):
                newNum.append((nums[x]+nums[x+1])%10)
            return newNum


        while len(newN)>1:
            n = GetNextSeries(newN)

            newN = n

        return(newN[-1])
    