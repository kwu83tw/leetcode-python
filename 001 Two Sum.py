'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_temp = dict()
        for index, value in enumerate(nums):
            if target - value in dict_temp:
                return [dict_temp[target - value], index]
            dict_temp[value] = index
            #print dict_temp


if __name__ == "__main__":
    #nums = [3, 2, 4]
    #target = 6
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
