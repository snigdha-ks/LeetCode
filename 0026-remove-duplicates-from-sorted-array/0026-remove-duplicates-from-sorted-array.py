class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0

        while i < n - 1:
            j = i + 1
            while j < n:
                if nums[i] == nums[j]:
                    nums.pop(j)
                    n -= 1  # Adjust the length after pop
                else:
                    j += 1
            i += 1

        return len(nums)