class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        st = []
        stocks_period = 0
        for x in range(len(prices)):
            cur = prices[x]
    
            if st and cur - st[-1]!=-1:
                cur_len =len(st)
                stocks_period+=((cur_len*(cur_len+1))//2)
                st=[]
            st.append(prices[x])

        stocks_period+=((len(st)*(len(st)+1))//2)

        return(stocks_period)