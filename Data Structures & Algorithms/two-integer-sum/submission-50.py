class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            d = target - v
            if d in hashmap:
                return [hashmap[d], i]
            hashmap[v] = i
            