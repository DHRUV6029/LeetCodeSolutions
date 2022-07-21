class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)

        if s%3!=0:
            return(False)
        
        t = s//3
        s=0
        c = 0
        for x in range(0, len(arr)):
            s+=arr[x]
            if s==t:
                c+=1
                s=0

        if c >=3:
            return(True)
        return(False)