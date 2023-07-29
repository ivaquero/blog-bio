#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for ind, num in enumerate(nums):
            if (target - num) in nums[ind + 1 :]:
                ind2 = nums.index(target - num, ind + 1)
                return [ind, ind2]

        return []
        # @lc code=end
