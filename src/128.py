class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Check if nums array is empty
        if not nums:
            return 0
        
        # Sort the array
        nums.sort()

        # Logic
        consecutives = 1
        longest_consecutive = 1
        current_top = nums[0]
        
        for num in nums:
            if num == current_top:
                continue

            if num == current_top + 1:
                consecutives += 1
                if consecutives >= longest_consecutive:
                    longest_consecutive = consecutives
            else:
                consecutives = 1

            current_top = num

        return longest_consecutive


def test_solution():
    solution = Solution()
    
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]

    print(solution.longestConsecutive(nums))


test_solution()