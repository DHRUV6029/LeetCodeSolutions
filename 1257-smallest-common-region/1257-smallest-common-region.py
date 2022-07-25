class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        neighbourSet = set()
        reigonDict = defaultdict()
        res = ''
        for reigon in regions:
            
            for x in range(1, len(reigon)):
                reigonDict[reigon[x]]=reigon[0]
        neighbourSet.add(region1)
        while region1 in reigonDict:
            neighbourSet.add(reigonDict[region1])
            region1 = reigonDict[region1]

        while region2 not in neighbourSet:
            region2 = reigonDict[region2]
    

        return(region2)