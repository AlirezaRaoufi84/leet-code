# 1- Two Sum
# we have a list and a target and we have to find the two elements that by adding them we reach our target.


def twoSum(nums, target):
    hash_int = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_int:
            return [hash_int[diff], i]
        else:
            hash_int[nums[i]] = i


nums = [2, 45, 5, 66, 7]
target = 12

twoSum(nums, target)  # [2 , 4]
