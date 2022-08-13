class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mp = defaultdict(list)
        rank  = [-1]*len(arr)
        rank_count = 1

        for x in range(0, len(arr)):
            mp[arr[x]].append(x)

        mp = dict(sorted(mp.items() , key=lambda x : x[0]))

        for k , v in mp.items():
            for i in v:
                rank[i] = rank_count
            rank_count+=1

        return(rank)