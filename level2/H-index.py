def solution(citations):
    i = 10000
    while True:
        up = 0
        down = 0
        for citation in citations:
            if citation >= i:
                up += 1
            else:
                down += 1

        if up >= i >= down:
            return i
        i -= 1
