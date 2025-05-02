class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = []

        for i in range(len(nums)):
            answer.append(1)

        for i in range(len(nums)):
            left, right = 1, 1

            while i - left >= 0:
                answer[i] *= nums[i-left]
                left += 1

            while i + right < len(nums):
                answer[i] *= nums[i+right]
                right += 1

        return answer
