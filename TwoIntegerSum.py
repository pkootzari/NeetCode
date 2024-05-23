from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            number = nums[i]
            if number in pairs:
                return [pairs[number], i]
            difference = target - number
            pairs[difference] = i
        