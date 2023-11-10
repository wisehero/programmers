from collections import Counter


def solution(str1, str2):
    s1_arr = []
    s2_arr = []

    for i in range(len(str1) - 1):
        a = str1[i:i + 2].lower()
        if a.isalpha():
            s1_arr.append(a)
    for i in range(len(str2) - 1):
        a = str2[i:i + 2].lower()
        if a.isalpha():
            s2_arr.append(a)

    if not s1_arr and not s2_arr:
        return 65536

    c1 = Counter(s1_arr)
    c2 = Counter(s2_arr)

    s1_inter_s2 = []
    s1_union_s2 = []
    for key in c1.keys():
        if c1[key] and c2[key]:
            m = min(c1[key], c2[key])
            n = max(c1[key], c2[key])
            while m:
                s1_inter_s2.append(key)
                m -= 1

            while n:
                s1_union_s2.append(key)
                n -= 1

    for key in s1_arr:
        if key not in s1_inter_s2:
            s1_union_s2.append(key)
    for key in s2_arr:
        if key not in s1_inter_s2:
            s1_union_s2.append(key)

    if s1_inter_s2 and s1_union_s2:
        r = len(s1_inter_s2) / len(s1_union_s2)
    else:
        return 0

    answer = 65536 * r
    return int(answer)
