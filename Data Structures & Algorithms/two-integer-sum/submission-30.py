class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            dif = target - v
            if dif in hashmap:
                return [hashmap[dif], i]
            hashmap[v] = i