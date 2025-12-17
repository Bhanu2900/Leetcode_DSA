class Solution:
    def mySqrt(self, x: int) -> int:
        # this solution uses inbuild function in python
        #other solution is result = x ** 0.5
        result = math.sqrt(x)
        return (int(result))