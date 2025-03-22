class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m =0
        for k in range(n):
            if nums[k] != 0:
                nums[m] = nums[k]
                m+=1
        for j in range(m,n):
            nums[j] = 0
        return nums
                
             
               