def solution(clothes):
    cloths = {}

    for name, kind in clothes:
        if kind in cloths:
            cloths[kind] += 1
        else:
            cloths[kind] = 1

    answer = 1
    for key, value in cloths.items():
        answer *= (value + 1)

    return answer - 1  # 모두 안입는 경우 빼기
