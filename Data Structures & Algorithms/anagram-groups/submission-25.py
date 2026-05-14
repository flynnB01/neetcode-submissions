class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sub = []
        for idx, i in enumerate(strs):
            if any(i in group for group in result):
                continue
            sub.append(i)
            i1 = sorted(i)
            for j in strs[idx + 1:]:
                if sorted(j) == i1:
                    sub.append(j)
            result.append(sub)
            sub=[]
        return result

