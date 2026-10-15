class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_list = []
        for i in s:
            S_list.append(i)
        for j in t:
            try:
                S_list.remove(j)
            except:
                return False
        if S_list == []:
            return True
        else:
            return False