def solution(number):
    answer = 0
    numbers = "1234567890"
    str = []
    for n in number:
        idx = numbers.index(n)
        if len(str) != 0 and numbers[idx] == str[-1] and numbers[idx] != "0":
            continue

        if numbers[idx] == "0":
            answer += 1
            str.append(numbers[idx])

        else:
            str.append(numbers[idx])
            str.append(numbers[idx + 1])
            answer += 1

        if str[-1] != number[:len(str)][-1]:
            str.pop()
            answer += 1

        if "".join(str) == number:
            print(answer)
            return answer


    return answer


solution("321")
