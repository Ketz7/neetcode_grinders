class Solution:
    def twoSum(self,nums, target):
        items = {}
        for index, value in enumerate(nums):
            if target - value in items:
                return [items[target - value], index]
            else:
                items[value] = index