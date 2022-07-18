class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1:
            return 10
        path = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        res = 0
        dp=[[0 for x in range(10)] for y in range(n+1)]
        mod = 1000000007
        for x in range(0 , 10):
            dp[1][x]=1

        for i in range(0 , n+1):
            for j in range(0 , 10):
                p = path[j]
                for k in p:
                    dp[i][j]+=dp[i-1][k]
                    dp[i][j] =dp[i][j]%mod


        return(sum(dp[-1])%mod)