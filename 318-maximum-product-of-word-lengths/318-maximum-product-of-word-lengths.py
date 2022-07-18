class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_mask = []
        max_res = 0


        for x in range(0  , len(words)):
            tmp = '00000000000000000000000000'
           
            for y in range(0 , len(words[x])):
                idx = ord(words[x][y])-97
                tmp = tmp[:idx]+'1'+tmp[idx+1:]
        
            bit_mask.append(int(tmp, 2))
    


        for i in range(len(bit_mask)):
            for j in range(i+1, len(bit_mask)):
                if (bit_mask[i] & bit_mask[j]==0):
                    max_res = max(max_res , len(words[i])*len(words[j]))

        return(max_res)
