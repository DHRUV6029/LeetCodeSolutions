class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        val = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o','p','q','r','s',
't', 'u', 'v', 'w', 'x', 'y', 'z']
        arr = [0]*n

        for x in range(0, len(arr)):
            max_possible = k - (n-(x+1))
            if max_possible>=26:
                arr[x] = val[26]
                k-=26
            else:
                arr[x] = val[max_possible]
                k-=(max_possible)

        return(''.join(arr[::-1]))