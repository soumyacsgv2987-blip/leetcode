class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store numbers we have already seen
        seen = {}
        
        # Go through each number in the list
        for i, num in enumerate(nums):
            # Calculate what matching number we need to hit the target
            remaining = target - num
            
            # If we already saw that matching number, return their positions
            if remaining in seen:
                return [seen[remaining], i]
                
            # Otherwise, remember this number and its position
            seen[num] = i
        