class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index, value in enumerate(nums):
            dif = target - value
            if dif in hashmap:
                return [hashmap[dif], index]
            hashmap[value] = index