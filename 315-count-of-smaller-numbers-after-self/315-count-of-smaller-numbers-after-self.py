class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr  =nums.copy()

        arr.sort()
        ans= []
        for n in nums:
            x = bisect_left(arr, n)
            ans.append(x)
            del arr[x]

        return(ans)