class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        l = 0
        ml = 0
        sub = set()

        while right < len(s):
            if s[right] not in sub:
                sub.add(s[right])
                l += 1
                right += 1
                if l > ml:
                    ml = l
            else:
                while s[right] in sub:
                    sub.remove(s[left])
                    if l > ml:
                        ml = l
                    l -= 1
                    left += 1
        return ml