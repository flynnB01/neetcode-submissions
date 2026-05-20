class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[', '}':'{'}
        ans = []
        for i in s:
            if i not in hashmap:
                ans.append(i)
            else:
                if len(ans) == 0:
                    print(len(ans), '1')
                    return False
                else:
                    popped = ans.pop()
                    if popped != hashmap[i]:
                        print(len(ans), '2')
                        return False
        print(len(ans), '3')
        return len(ans) == 0

