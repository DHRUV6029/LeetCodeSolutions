class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        l = 0
        r = l+1
        nums.sort()
        res = set()
        while r < len(nums) and l<=r:
            if abs(nums[l]-nums[r])==k and l!=r:
                res.add((nums[l], nums[r]))
                l+=1
                r+=1
            elif abs(nums[l]-nums[r]) > k:
                l+=1
            else:
                r+=1
        
        return(len(res))