class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_sq(num: int) -> int:
            return sum(int(digit)** 2 for digit in str(num))
        cycle = set()

        while  n != 1 and n not in cycle:
            cycle.add(n)
            n = sum_sq(n)
        return n == 1
