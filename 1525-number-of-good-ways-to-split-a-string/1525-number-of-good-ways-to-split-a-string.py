class Solution:
    def numSplits(self, s: str) -> int:
        mpl = defaultdict()
        mpr = defaultdict()

        mpr = Counter(s) # currenlty all in mpr
        count = 0
        for x in range(0, len(s)):
            if not s[x] in mpl:
                mpl[s[x]] = 1
            else:
                mpl[s[x]]+=1
    
            if s[x] in mpr:
                mpr[s[x]]-=1
            if mpr[s[x]]==0:
                mpr.pop(s[x])
    
            if len(mpl) == len(mpr):
                count+=1

        return(count)
