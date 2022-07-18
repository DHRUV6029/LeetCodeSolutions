class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(s=0, cur =[]):
            if len(cur)==k:
                return out.append(cur[:])
            for c in range(s, n):
                cur.append(nums[c])
                
                backtrack(c+1, cur)
                
                cur.pop()
                
                
        out =[]
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return out
        