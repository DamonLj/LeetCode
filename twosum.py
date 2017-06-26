#!/user/bin/env python
#_*_coding:utf-8_*_

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        gap = int(len(nums) // 2)
        while gap > 0:
            for i in range(gap, len(nums)):
                for j in range(0, i-gap+1, gap):
                    if nums[i] + nums[j] == target:
                        return (sorted([i, j]))
            gap = gap // 2

if __name__ == '__main__':
    print(Solution().twoSum([2, 15, 4, 6, 44, 23, 44, 4, 7], 9))
