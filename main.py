def solution(num, total):
    nums = [x for x in range(-1000, 1000)]
    i = 0
    while True:
        if sum(nums[i:i + num]) == total:
            return nums[i:i + num]
        else:
            i += 1

    return answer