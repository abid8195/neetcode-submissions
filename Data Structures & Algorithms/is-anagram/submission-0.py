class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for m in s:
            if m in s1:
                s1[m] += 1
            else:
                s1[m] = 0
        for n in t:
            if n in s2:
                s2[n] += 1
            else:
                s2[n] = 0
        if s1 == s2:
            return True
        else:
            return False
        