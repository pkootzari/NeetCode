from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        
        frequency_sorted = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in frequency_sorted[:k]]