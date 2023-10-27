def solution(s):
    arr1 = s.split(" ")
    arr2 = []

    for a in arr1:
        arr2.append(int(a))

    return str(min(arr2)) + " " + str(max(arr2))