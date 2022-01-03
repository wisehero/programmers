def solution(n, arr1, arr2):
    answer = []
    check = ''
    for i in arr1:
        binary = bin(i)[0] + bin(i)[2:]
        if len(binary) > n:
            binary = binary[1:]
        else:
            binary = binary.rjust(n, "0")
        for j in binary:
            if j == "0":
                check += " "
            else:
                check += "#"
        answer.append(check)
        check = ''
    print(answer)
    for i in range(len(arr2)):
        binary = bin(arr2[i])[0] + bin(arr2[i])[2:]
        if len(binary) > 5:
            binary = binary[1:]
        else:
            binary = binary.rjust(n, "0")
        check_map = list(answer[i])
        for j in range(len(binary)):
            if check_map[j] == " " and binary[j] == "1":
                check_map[j] = "#"
        answer[i] = "".join(check_map)
    return answer


def optimalsolution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
