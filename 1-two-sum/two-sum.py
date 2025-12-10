class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# Bhanu
        num_ber = {}
        for i, num in enumerate(nums):
            new = target - num
            if new in num_ber:
                return[num_ber[new], i]
            num_ber[num] = i