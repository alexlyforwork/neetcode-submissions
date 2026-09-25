class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_w = ''.join(sorted(word))
            groups[sorted_w].append(word)
        return list(groups.values())