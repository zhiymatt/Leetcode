#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (44.31%)
# Total Accepted:    104.8K
# Total Submissions: 236.6K
# Testcase Example:  '[1,1]'
#
# 
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# 
# 
# Note:
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        walker = runner = 0
        while walker != runner or walker == 0:
            print('running: ', walker, runner)
            walker = nums[walker]
            runner = nums[nums[runner]]
        print(walker, runner)
        crawler = 0
        while walker != crawler:
            walker = nums[walker]
            crawler = nums[crawler]
        print(crawler, walker)
        return walker
