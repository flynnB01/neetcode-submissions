class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, v in enumerate(nums):
            b = target - v
            if b in hashmap:
                return [hashmap[b], i]
            hashmap[v] = i