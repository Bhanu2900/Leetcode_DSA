class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # here we take all the non- zeros values by comparing, save them first and then add all the remaing zeros to the end with the help of the loop
        """
        Do not return anything, modify nums in-place instead.
        """
        b = 0 
        for a in range(len(nums)):
            if nums[a] != 0:
                nums[b] = nums[a]
                b += 1
        while b < len(nums):
            nums[b] = 0
            b += 1

