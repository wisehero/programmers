def solution(quiz):
    answer = []

    for i in range(len(quiz)):
        expression = quiz[i].split(" ")
        operand1, operator, operand2, result = int(expression[0]), expression[1], int(expression[2]), int(expression[4])
        if operator == "+":
            if operand1 + operand2 == result:
                answer.append("O")
            else:
                answer.append("X")

        else:
            if operand1 - operand2 == result:
                answer.append("O")
            else:
                answer.append("X")
    return answer