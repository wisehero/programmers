from collections import deque


def solution(msg):
    answer = []
    msg = deque(msg)
    check = deque([])
    alphabet = ["0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    while True:
        check.append(msg.popleft())
        new_word = "".join(check)
        if new_word not in alphabet:
            alphabet.append(new_word)
            answer.append(alphabet.index(check[0]))
            check.popleft()
        else:
            check = deque([])
            check.append(new_word)
        if len(msg) == 0:
            answer.append(alphabet.index(check[0]))
            break

    return answer


solution("ABABABABABABABAB")
