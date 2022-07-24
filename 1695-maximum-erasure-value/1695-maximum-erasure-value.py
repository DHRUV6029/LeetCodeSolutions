class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mp  = set()
        l = 0
        cur_sum =0
        max_sum = 0
        for x in range(0 , len(nums)):
            while nums[x] in mp:
                cur_sum-=nums[l]
                mp.remove(nums[l])
                l+=1
            cur_sum+=nums[x]
            mp.add(nums[x])
            max_sum = max(max_sum , cur_sum)

            max_sum = max(max_sum ,cur_sum)
            
        return max_sum