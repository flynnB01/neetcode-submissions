class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[left] + nums[i] + nums[right]
                if s == 0:
                    ans.append([nums[left], nums[i], nums[right]])

                    left_val = nums[left]
                    right_val = nums[right]
                    while left < right and right_val == nums[right]:
                        right -= 1
                    while left < right and left_val == nums[left]:
                        left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return ans

