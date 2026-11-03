# Missing number


def missing_number(nums):
    missing = 0
    for num in nums:
        missing ^= num
    for num in range(len(nums) + 1):
        missing ^= num
    return missing
