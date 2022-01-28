def solution(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        answer = 1
    str1 = str1.upper()
    str2 = str2.upper()
    answer = 0
    inter = []
    str1_lst = []
    str2_lst = []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            str1_lst.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            str2_lst.append(str2[i:i + 2])

    a = str1_lst.copy()
    b = str2_lst.copy()

    # 다중 집합의 교집합
    for i in str1_lst:
        if i in b:
            inter.append(i)
            a.remove(i)
            b.remove(i)

    # 다중 집합의 합집합
    str1_lst_temp = str1_lst.copy()
    uni = str1_lst.copy()

    for i in str2_lst:
        if i not in str1_lst_temp:
            uni.append(i)
        else:
            str1_lst_temp.remove(i)

    if len(uni) == 0:
        answer = 65536
        return answer

    answer = int(((len(inter) / len(uni)) * 65536))
    return answer


print(solution("asdf", "zxcv"))
