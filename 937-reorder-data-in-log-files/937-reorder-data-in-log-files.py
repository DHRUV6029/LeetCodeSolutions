class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        mp = defaultdict(list)
        for log in logs:
            if log.split(' ')[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        tmp = []
        for l in letter:
            mp[l.split(' ', maxsplit=1)[1]].append(l.split(' ' , maxsplit=1)[0])

        mp = dict(sorted(mp.items(), key=lambda x : x[0]))

        for k , v in mp.items():
            if len(v)>1:
                v.sort()
            for it in v:
                tmp.append(it+' '+k)

        return(tmp+digit)