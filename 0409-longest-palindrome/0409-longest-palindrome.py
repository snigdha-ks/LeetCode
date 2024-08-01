class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_c= {}
        for char in s:
            if char in char_c:
                char_c[char]+=1
            else:
                char_c[char]=1
        length=0
        odd = False
        for i in char_c.values():
            length += (i//2) * 2
            if i%2 ==1:
                odd= True
        if(odd):
            length+=1
        return length



        