class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        idx = 0
        A=0
        B =0
        aliceTotal = 0
        bobTotal = 0 
        if len(colors)<3:
            return False

        while idx < len(colors):
            while  idx<len(colors) and colors[idx]=='A':
                A+=1
                alice = max(alice,A )
                idx+=1
            if alice>=3:
                aliceTotal+=(alice-2)
                alice = 0
    
            while idx<len(colors) and colors[idx]=='B':
                B+=1
                bob = max(bob, B)
                idx+=1
            if bob>=3:
                bobTotal+=(bob-2)
                bob =0 
            A=0
            B=0


        if aliceTotal<=bobTotal:
            return(False)
        else:
            return(True)