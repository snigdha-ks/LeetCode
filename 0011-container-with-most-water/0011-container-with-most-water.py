class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a= 0
        n = len(height)
        left = 0
        right = n-1
        while (left<right):
            temp = min(height[left],height[right]) * (right - left)
            if temp > a:
                a = temp
            if height[left] <height[right]:
                left +=1
            else:
                right -=1
        return a