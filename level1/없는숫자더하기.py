def solution(numbers):
    s1 = set([1,2,3,4,5,6,7,8,9,0])
    s2 = set(numbers)
    return sum(s1-s2)