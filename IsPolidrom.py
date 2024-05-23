from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        hashset = {}
        for index, i in enumerate(nums):
            hashset[i] = hashset.get(i, set([])).union(set([index]))

        # print(hashset)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                numi = nums[i]
                numj = nums[j]
                k = -(numi+numj)
                if k in hashset:
                    indecies = set(hashset[k])
                    uniqIndices = sorted(list(indecies - set([i, j])))
                    if len(uniqIndices) > 0 and uniqIndices[0] > j:
                        results.append([numi, numj, k])

        return results
        

# sol = Solution()
# print(sol.threeSum([-1,0,1,2,-1,-4]))
