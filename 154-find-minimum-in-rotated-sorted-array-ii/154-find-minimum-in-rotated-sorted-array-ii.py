class Solution:
    def findMin(self, nums: List[int]) -> int:
        cur_min = nums[0]
        
            

        for x in range(0, len(nums)-1):
            if nums[x]>=nums[x+1]:
                cur_min = min(cur_min , nums[x+1])

        return(cur_min)