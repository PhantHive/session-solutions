"""
Exercise: Two Sum
Goal: Given a list of numbers and a target number,
return the indices of two numbers in the list that add up to the target number.
"""


def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
    return False


print(twoSum([2, 7, 11, 15], 9))
# 0, 1 because nums[0] + nums[1] = 2 + 7 = 9
