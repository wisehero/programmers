def solution(s):
    answer = ''

    d = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
         "eight": "8", "nine": "9", "zero": "0"}
    word = ''

    for a in s:
        if word in d:
            answer += d[word]
            word = ''

        if a.isdigit():
            answer += a
        else:
            word += a

    if word:
        answer += d[word]

    return int(answer)
