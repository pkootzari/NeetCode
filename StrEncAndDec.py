from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded = encoded + str(length) + "&" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            lengthStr = ""
            while s[i] != "&":
                lengthStr += s[i]
                i += 1
            length = int(lengthStr)
            string = ""
            i += 1 
            for j in range(length):
                string = string + s[i]
                i += 1
            strs.append(string)
        return strs
    

# Input = ["neet","code","love","you"]
# sol = Solution()
# enc = sol.encode(Input)
# print(enc)
# dec = sol.decode(enc)
# print(dec)

