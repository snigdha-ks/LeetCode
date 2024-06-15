class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x< 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        rev = ''
        for char in str(x):
            rev = char + rev
        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31  

        if int(rev) >  INT_MAX  or  int(rev) < INT_MIN :
            return 0
        
        return int(rev) * sign
