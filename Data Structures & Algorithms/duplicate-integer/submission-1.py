class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = list(set(nums))
        if len(nums) == len(unique):
            return False
        else:
            return True