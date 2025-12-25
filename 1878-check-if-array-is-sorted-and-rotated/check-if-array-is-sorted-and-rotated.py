class Solution:
    def check(self, nums: List[int]) -> bool:
        # bhanu
        count = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False
            i += 1

        return True
        