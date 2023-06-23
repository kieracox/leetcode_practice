class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in anagram_groups:
                anagram_groups[sorted_str] = []
            anagram_groups[sorted_str].append(string)
           
        result = list(anagram_groups.values())
        return result
