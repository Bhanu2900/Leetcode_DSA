class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_sq(num: int) -> int:
            return sum(int(digit)** 2 for digit in str(num))
        while  n != 1 and n != 4:
            n = sum_sq(n)
        return n == 1
