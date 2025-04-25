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
        curr_sum = 0
        for i in range(length):
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum
