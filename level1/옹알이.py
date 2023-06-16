def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for s in can_speak:
            if s in babbling[i]:
                babbling[i] = babbling[i].replace(s, 'z')
        print(babbling)

        st = list(set(babbling[i]))
        if len(st) == 1 and st[0] == "z":
            answer += 1
    return answer



def best_solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c
