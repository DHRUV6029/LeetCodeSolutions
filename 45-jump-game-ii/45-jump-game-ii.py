class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0 
        
        while r < len(nums)-1:
            farJump= 0
            for x in range(l , r+1):
                farJump = max(farJump, x+nums[x])
            l=r+1
            r = farJump
            
            res+=1
            
        return res