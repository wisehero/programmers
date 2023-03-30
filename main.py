from collections import Counter


def singleNumber(nums):
    answer = 0
    counter = Counter(nums).most_common()
    return counter[-1][0]


singleNumber([4, 1, 2, 1, 2])
