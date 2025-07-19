class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
    
        for start in range(n):
            curr_sum = 0
            for end in range(start, n):
                curr_sum += nums[end]
                if curr_sum == k:
                    count += 1
    
        return count