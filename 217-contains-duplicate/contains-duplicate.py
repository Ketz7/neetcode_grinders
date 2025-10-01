class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x= {}
        for num in nums:
            if num in x and x[num] >= 1:
                return True
            x[num] = 1
        return False