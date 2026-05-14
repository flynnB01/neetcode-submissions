class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for i in nums:
            if i in arr:
                print(nums, i)
                return True
            arr.append(i)
        return False