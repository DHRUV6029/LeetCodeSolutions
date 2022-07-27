class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = defaultdict()
        res = []
        for domain in cpdomains:
            freq = domain.split(' ')
            dotCounter = Counter(freq[1])
            for x in range(0 , dotCounter['.']+1):
                subdomains = freq[1].split('.', x)[-1]
                if subdomains in mp:
                    mp[subdomains]+=(int(freq[0]))
                else:
                    mp[subdomains] = int(freq[0])


        for k , v in mp.items():
            res.append(str(v)+" "+k)

        return(res)