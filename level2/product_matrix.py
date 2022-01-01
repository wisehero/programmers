"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수,
solution을 완성해주세요.
"""


def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp_lst = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            temp_lst.append(temp)
        answer.append(temp_lst)

    return answer


arr1 = [
    [1, 4],
    [3, 2],
    [4, 1]
]

arr2 = [
    [3, 3],
    [3, 3]
]

print(solution(arr1, arr2))
