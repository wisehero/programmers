def solution(n, words):
    checked = set()
    i = 0
    while i < len(words):
        if words[i] in checked:
            return [i % n + 1, i // n + 1]

        if i > 0 and words[i][0] != words[i - 1][-1]:
            return [i % n + 1, i // n + 1]

        checked.add(words[i])

        i += 1

    return [0, 0]
