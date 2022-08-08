class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph =paragraph.lower().replace('!', ' ').replace('?', ' ').replace(',', ' ').replace('.',' ').replace("'",' ').replace(';',' ')
        arr = paragraph.split(" ")
        s_res = sorted(Counter(arr).items() , key=lambda a : a[1], reverse=True)


        for x in s_res:
            if x[0] not in banned and x[0]!= '':
                return x[0]