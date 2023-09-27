def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1_e = list(str(bin(arr1[i])[2:]).zfill(n))
        arr2_e = list(str(bin(arr2[i])[2:]).zfill(n))
        code = ''

        for j in range(len(arr1_e)):
            code += max(arr1_e[j], arr2_e[j])

        e = ''
        for c in code:
            if c == '1':
                e += "#"
            else:
                e += ' '

        answer.append(e)
    return answer
