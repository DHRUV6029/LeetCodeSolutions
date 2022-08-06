class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        cur_max = nums[0]
        poss_max = nums[0]
        c=1
        for x in range(0,len(nums)):
            if cur_max>nums[x]:
                c =x+1
                cur_max = poss_max
            else:
                poss_max = max(poss_max , nums[x])

        return(c)