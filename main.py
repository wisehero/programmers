import math
def solution(n):
    for i in range(1, 11):
        if (i+1) *math.factorial(i) >  n:
            return i