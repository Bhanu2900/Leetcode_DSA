class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid  = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                l = mid + 1
            else:
                r = mid -1
        return -1

        #here we take two pointing values  left and right, run a loop for the sorted array{ left <= right}, taking middle element { mid = (left+rigt)/ 2}, now if mid = target return mid, if mid<target , search left {left = mid +1}, if mid>right search right { right = mid +1}  if found return -1