
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # If the unique count doesn't match the original count, duplicates xist
        return len(nums) != len(set(nums))

        