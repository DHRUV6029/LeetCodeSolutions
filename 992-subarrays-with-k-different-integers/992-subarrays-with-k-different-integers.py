class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def AtMostDistinct(nums,k):
            l = 0 
            r = 0
            mp = defaultdict()
            res = 0 

            while r < len(nums):
                if nums[r] not in mp:
                    mp[nums[r]] = 0 
        
                mp[nums[r]]+=1

                while len(mp) > k:
                    mp[nums[l]]-=1
                    if mp[nums[l]]==0:
                        mp.pop(nums[l])
                    l+=1

                res+=(r-l+1)
                r+=1
            return res
        
        return AtMostDistinct(nums,k)-AtMostDistinct(nums,k-1)