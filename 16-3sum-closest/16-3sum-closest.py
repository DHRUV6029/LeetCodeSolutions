class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = float('-inf')
        mini =float('inf')
        res =0 
        for x in range(0 , len(nums)-1):
            l =x+1
            r=len(nums)-1

            while l < r:
                cur_sum = nums[x]+nums[l]+nums[r]
                closet = abs(target-cur_sum)

                if closet<mini:
                    res = cur_sum
                    mini =closet
        
                elif cur_sum==target:
                    return (target)
            
                elif cur_sum>target:
                    r-=1
                else:
                    l+=1

        return(res)
