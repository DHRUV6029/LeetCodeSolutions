class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        #backchodi hai yeh saab
        if len(num1) > len(num2):
            for _ in range(0, len(num1)-len(num2)):
                num2 = '0' + num2
        elif len(num2) > len(num1):
            for _ in range(0 , len(num2)-len(num1)):
                num1 = '0' + num1


        # real code starts

        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        for x in range(len(num1)):
            v1 = int(num1[x])
            v2 = int(num2[x])

            r = carry +v1+v2
            carry = r//10
            res+=(str(r%10))

        if carry>0:
            res+='1'
            
            
            
            
        return res[::-1]


