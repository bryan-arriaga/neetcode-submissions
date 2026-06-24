class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for str in strs:
            word = ''.join(sorted(str))
            map[word].append(str)
        
        return map.values()
        