class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1

            n >>= 1
        return count


        # here we use the bitwies and operator" & "  to count the number's  the output of the is 1 if there is 1,1 
        # and for there the 0,0 and 1,0 give 0 if n >=1coiunt +1
        