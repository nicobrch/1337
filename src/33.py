class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def bs(arr, low, high, target):
            if high >= low:
                mid = (high + low) // 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return bs(arr, low, mid-1, target)
                else:
                    return bs(arr, mid+1, high, target)

            else:
                return -1

        original_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                original_index = i

        nums.sort()

        result = bs(nums, 0, len(nums)-1, target)

        return result if result == -1 else result + original_index
