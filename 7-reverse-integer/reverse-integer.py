class Solution:
    def reverse(self, x: int) -> int:
         max = 2**31-1
         min = -2**31
         is_negative = x < 0
         n = abs(x)
         rev_num = 0
         while n != 0:
            last_digit = n % 10
            n //= 10
            if rev_num > max//10:
                return 0
            rev_num = rev_num*10 + last_digit
         if is_negative:
            rev_num = -rev_num
         return rev_num



