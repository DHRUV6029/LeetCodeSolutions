class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cd = defaultdict(lambda:0)
        res = 0

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                s = nums3[i]+nums4[j]

                if s in cd:
                    cd[s]+=1
                else:
                    cd[s] = 1


        for k in range(0 , len(nums1)):
            for l in range(0 ,len(nums2)):
                ns = -(nums1[k]+nums2[l])
        
                if ns in cd:
                    res+=cd[ns]


        return(res)
        