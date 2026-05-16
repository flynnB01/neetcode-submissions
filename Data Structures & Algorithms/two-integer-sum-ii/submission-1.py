class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(numbers):
            d = target - v
            if d in hashmap:
                return [hashmap[d] + 1, i + 1]
            hashmap[v] = i