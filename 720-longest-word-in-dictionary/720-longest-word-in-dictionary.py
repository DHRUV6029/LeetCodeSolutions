class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        ans = ''
        wordset = set(words)

        for w in words:
            if len(w)>len(ans) or len(w)==len(ans) and w <ans:
                if all(w[:k] in wordset for k in range(1 , len(w))):
                    ans = w

        return(ans)