class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = 0
        num = 0
        ans = []
        for j in range(k):
            for i in nums:
                current = nums.count(i)
                if temp < current and i not in ans:
                    temp = current
                    num = i
            ans.append(num)
            temp = 0
            num = 0
        return ans

            


