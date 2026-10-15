class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        need ={}
        for i in s:
            need[i] = need.get(i,0)+1
        for i in t:
            need[i] = need.get(i,0)-1
        for i in need:
            if need[i] != 0:
                return False

        return True