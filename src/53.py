class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 1:
            return nums[0]

        max_sum = nums[0]
        for i in range(length):
            curr_sum = 0
            for j in range(i, length):
                curr_sum = curr_sum + nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum
