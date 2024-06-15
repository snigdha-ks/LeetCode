class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=0
        nums =nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 ==1:
            median =nums[n//2]
        else:
            median = (nums[(n//2) -1] + nums[n//2]) / 2.0
        return median