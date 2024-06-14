class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target in nums:
                if nums[i]==target:
                    return i
            elif nums[i]>target:
                nums.insert(i,target)
                return i
    
        nums.append(target)
        return len(nums) - 1
    