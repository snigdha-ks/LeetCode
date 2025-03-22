class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = 0
        t1 = 0
        while (s1< len(s) and t1< len(t)):
            if s[s1] == t[t1]:
                s1 +=1
            t1 +=1
        return s1 == len(s)

