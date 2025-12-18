class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n * (n + 1) // 2
        real_sum = sum(nums)
        return exp_sum - real_sum