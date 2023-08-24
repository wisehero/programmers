from itertools import permutations


def solution(expression):
    answer = 0

    # 수식 뽑아내기
    operator = set()
    for s in expression:
        if s in "*+-":
            operator.add(s)

    op_perm = list(permutations(operator, len(operator)))
    expression_list = []

    el = ""
    for i in range(len(expression)):
        if expression[i].isdigit():
            el += expression[i]
        else:
            expression_list.append(int(el))
            expression_list.append(expression[i])
            el = ''
    expression_list.append(int(el))

    for op_case in op_perm:
        li1 = expression_list
        li2 = []

        for op in op_case:
            i = 0
            while i < len(li1):
                if li1[i] == op:
                    if op == "*":
                        li2.append(li2.pop() * li1[i + 1])
                        i += 2
                    elif op == "-":
                        li2.append(li2.pop() - li1[i + 1])
                        i += 2
                    else:
                        li2.append(li2.pop() + li1[i + 1])
                        i += 2
                else:
                    li2.append(li1[i])
                    i += 1
            li1 = li2
            li2 = []
        answer = max(answer, abs(li1[0]))
    print(answer)
    return answer



solution("50*6-3*2")
