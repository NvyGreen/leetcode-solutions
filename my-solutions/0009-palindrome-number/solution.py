class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # x_str = str(x)
        # rev_x = x_str[::-1]
        # return x_str == rev_x

        if x < 0:
            return False

        copy_x = x
        rev_x = 0

        while copy_x != 0:
            digit = copy_x % 10
            rev_x = rev_x * 10 + digit
            copy_x //= 10
        
        return rev_x == x
        
