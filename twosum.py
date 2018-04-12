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
import time

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return i, dic[target - nums[i]]
            dic[nums[i]] = i
