class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rn = 0
        num = x
        while num != 0:
            rn = rn * 10 + num % 10
            num = num //10
        return rn == x
            
                

            
        