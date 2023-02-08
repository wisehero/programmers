from collections import Counter

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
            "apple", "banana"]


def solution(want, number, discount):
    answer = 0
    index = 0
    dic = dict()
    # 할인할 때 사고자하는 품목들의 갯수를 맵으로 저장
    while index < len(number):
        dic[want[index]] = number[index]
        index += 1

    # 딕셔너리끼리는 같은 지 안 같은 지 바로 비교 가능
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i + 10]):
            answer += 1

    return answer


print(solution(want, number, discount))
