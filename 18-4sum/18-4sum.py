class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for x in range(0 , len(nums)-3):
            for y in range(x+1, len(nums)-2):

                val = target -(nums[x]+nums[y])
                l = y+1
                r = len(nums)-1

                while l<r:
                    if nums[l] + nums[r]<val:
                        l+=1
                    elif nums[l] + nums[r] > val:
                        r-=1
                    else:
                        res.add((nums[x] , nums[y] , nums[l] , nums[r]))
                        l+=1
                        r-=1

        return(list(res))