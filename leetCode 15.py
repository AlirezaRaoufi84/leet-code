# 15 - 3 sum
"""
def threeSum(nums: list[int]) -> list[list[int]]:
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])

                    if triplet not in result:
                        result.append(triplet)

    return result


nums = [-1, 0, 1, 2, -1, -4]

result = threeSum(nums)
print(result)

correct but high runtime***
"""


def threesum(nums):
    nums.sort()
    answer = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1

            else:
                triple = [nums[i], nums[l], nums[r]]
                answer.append(triple)
                while l < r and nums[l] == triple[1]:
                    l += 1
                while l < r and nums[r] == triple[2]:
                    r -= 1
    return answer


nums = [-1, 0, 1, 2, -1, -4]

result = threesum(nums)
print(result)
