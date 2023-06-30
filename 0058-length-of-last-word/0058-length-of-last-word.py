class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        stripped_s = s.strip()

        word_list = stripped_s.split(" ")

        return len(word_list[-1])