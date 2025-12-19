class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            
            # If the current number matches the candidate, increment the count
            if candidate == num:
                count += 1
            # Otherwise, decrement the count
            else:
                count -= 1
        
        # The remaining candidate is the majority element
        return candidate
