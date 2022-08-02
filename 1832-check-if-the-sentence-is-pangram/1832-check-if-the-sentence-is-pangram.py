class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mp = defaultdict()

        for s in sentence:
            if s in mp:
                mp[s]+=1
            else:
                mp[s]=1

        if len(mp)==26:
            return(True)

        return(False)