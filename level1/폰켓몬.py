def solution(nums):
    kind = len(nums) // 2
    poke = set(nums)

    if len(poke) > kind:
        return kind
    else:
        return len(poke)
