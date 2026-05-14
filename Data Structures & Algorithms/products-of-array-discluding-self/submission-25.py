class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                temp *= nums[j]
            result.append(temp)
        return result
        
