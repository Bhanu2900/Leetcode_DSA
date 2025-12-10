class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rn = 0
        num = x
        while num >0:
            ld = num % 10
            num //= 10
            rn = rn * 10 + ld
        return rn == x
            
                

            
        