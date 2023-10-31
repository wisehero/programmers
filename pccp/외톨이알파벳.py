def solution(input_string):
    answer = ''
    arr = []

    string = input_string[0]
    for s in input_string[1:]:

        if s == string:
            string += s
        else:
            arr.append(string)
            string = s

    print(arr)
    return answer


solution("edeaaabbccd")