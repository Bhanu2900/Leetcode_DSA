class Solution:
    def reverseString(self, s: List[str]) -> None:

        # left = left most element index,  right = right most element index
        """
        Do not return anything, modify s in-place instead.
        """
        left , right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1