class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root  = int(math.sqrt(num))
        if root * root == num:
            return True
        return False