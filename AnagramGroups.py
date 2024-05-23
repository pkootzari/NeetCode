from typing import NewType, Dict, List

CharDict = NewType('CharDict', Dict[str, int])
Strings = NewType('Strings', List[str])
ListOfStrings = NewType('ListOfStrings', List[Strings])
DictOfCharDict = NewType('DictOfCharDict', Dict[CharDict, Strings])

class Solution:
    def getDictofChars(self, string: str) -> CharDict:
        dictofChars = {}
        for ch in string:
            dictofChars[ch] = dictofChars.get(ch, 0) + 1
        return dictofChars

    def convertGroupsDictToList(self, groups: DictOfCharDict) -> ListOfStrings:
        listOfStrings = []

        for _, value in groups.items():
            listOfStrings.append(value)

        return listOfStrings

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # dict_of_chars -> list_of_strings
        for string in strs:
            chars = self.getDictofChars(string)
            hashable_chars = frozenset(chars.items())
            groups[hashable_chars] = groups.get(hashable_chars, list([])) + [string]

        listOfStrings = self.convertGroupsDictToList(groups)
        return listOfStrings

        

# strs = ["act","pots","tops","cat","stop","hat"]

# sol = Solution()
# result = sol.groupAnagrams(strs)
# print(result)