class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        val = x
        while x > 0:
            v = x%10
            x = x//10
            res = res*10 + v
            
        if res == val:
            return True
        else:
            return False
            