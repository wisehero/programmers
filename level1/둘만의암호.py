def solution(s, skip, index):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for i in skip:
        if i in alphabet:
            alphabet.remove(i)
    answer = ''
    s = list(s)
    for i in range(len(s)):
        # index 만큼 뒤에 있는 문자
        s[i] = alphabet[(alphabet.index(s[i]) + index) % len(alphabet)]
    answer = "".join(s)
    return answer


print(solution("aukks", "wbqd", 5))
