class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = []
    answer = ''
    for i in S:
        if i in prec:
            if len(opStack) != 0 and prec[opStack[-1]] >= prec[i] and i != "(":
                while len(opStack) != 0:
                    answer += opStack.pop()
                    if len(opStack) >= 1 and prec[opStack[-1]] < prec[i]:
                        break
                opStack.append(i)
            else:
                opStack.append(i)
        elif i == ")":
            while opStack[-1] != "(":
                answer += opStack.pop()
            opStack.pop()
        else:
            answer += i
    while len(opStack) != 0:
        answer += opStack.pop()
    return answer


print(solution("A+B*C-D/E"))
