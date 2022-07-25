class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = Counter(text)

        ans = [word['b'], word['a'] , word['l']//2 , word['o']//2 , word['n']]
        return(min(ans))
