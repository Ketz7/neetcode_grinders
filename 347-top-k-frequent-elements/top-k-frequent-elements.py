class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for number, value in count.items():
            frequency[value].append(number)

        result = []
        
        for i in range(len(frequency) -1, 0 , -1):
            for value in frequency[i]:
                result.append(value)
                if len(result) == k:
                    return result