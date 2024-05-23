class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sChars = {}
        for ch in s:
            if ch in sChars:
                sChars[ch] += 1
            else:
                sChars[ch] = 1
        
        for ch in t:
            if ch in sChars and sChars[ch] > 0:
                sChars[ch] -= 1
            else:
                return False

        return True
        