class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_num = str(x)

        if str_num == str_num[::-1]:
            return True
        
        return False