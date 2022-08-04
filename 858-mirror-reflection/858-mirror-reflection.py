class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
      


        def GetGcd(a , b):
            if a==0:
                return b
            return GetGcd(b%a ,a)


        v = p*q
        gcd =  GetGcd(p , q)
        lcm = v//gcd

        m = lcm//p
        n = lcm//q

        if m%2!=0 and n%2!=0:
            return 1
        elif m%2!=0 and n%2==0:
            return 2
        elif m%2==0 and n%2!=0:
            return 0
        
        return
