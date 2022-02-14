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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        # 피연산자이면 리스트에 추가
        if type(token) is int:
            postfixList.append(token)

        # '('이면 스택에 push
        elif token == '(':
            opStack.push(token)

        # ')' 이면 '('가 나올때까지 pop
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()

        # 연산자이면 +-*/
        else:
            # 스택이 비어있을 경우 스택에 push
            if opStack.isEmpty():
                opStack.push(token)

            # 스택이 비어있지 않다면 비교
            else:

                # 스택에 값이 존재할 동안에 반복
                while opStack.size() > 0:
                    # 우선 순위가 스택안에 있는게 높으면 꺼낸다
                    if prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    else:
                        break

                opStack.push(token)

    # 반복문을 다 돌고 스택이 빌때까지 pop
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    # 리스트로 리턴한다
    return postfixList


# 후위 표기법을 계산하는 함수
def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        # 피연산자를 만나면 스택에 push
        if type(token) is int:
            valStack.push(token)

        # 연산자를 만나면
        elif token == '+':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 + n1)

        elif token == '-':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 - n1)

        elif token == '*':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 * n1)

        elif token == '/':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(int(n2 / n1))

    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
