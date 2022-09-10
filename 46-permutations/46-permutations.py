class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i=0):
            if i == len(nums):
                res.append(nums[:])
                
            for x in range(i , len(nums)):
                nums[i] , nums[x] = nums[x] , nums[i]
                backtrack(i+1)
                nums[i] , nums[x] = nums[x] , nums[i]
                
                
                
        backtrack()
        return res
            