# O(n)
def twoSum_map(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - i], i]
        nums_map[num] = i


# Nlogn
def twoSum_two_pointer(nums, target):
    answer = []
    two_pointer = sorted(nums)
    s = 0
    e = len(nums) - 1
    while s != e:
        if two_pointer[s] + two_pointer[e] > target:
            e -= 1
        elif two_pointer[s] + two_pointer[e] < target:
            s += 1
        else:
            break
        answer.append(nums.index(two_pointer[s]))
        answer.append(nums.index(two_pointer[e]))
        return answer
