## 내 풀이
def solution(strings, n):
    strings = strings.sort()  # 선정렬
    for i in range(len(strings)):
        if i == len(strings) - 1:  # 인덱스 범위 넘어가는 것 방지
            break;
        if strings[i][n] > strings[i + 1][n]:  # n에 따라 자리 교환
            strings[i], strings[i + 1] = strings[i + 1], strings[i]
    return strings


# 다른 사람 풀이
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])
