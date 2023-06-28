class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        formatted = ""

        for char in s:
           if char.isalnum():
               formatted += char.lower()
        
        return formatted == formatted[::-1]