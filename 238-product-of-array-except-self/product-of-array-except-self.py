# Think about this in prefix and suffix array

# Prefix = [1, 2, 6, 24]

# Postfix = [24, 24, 12, 4]

# To save space we just use the answer array to store the prefix and multiply it backwards with the postfix to get the resultant array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer