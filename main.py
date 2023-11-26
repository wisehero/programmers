t = int(input())
ans = 0
for _ in range(t):
    s = list(input())

    f = True
    stack = []
    st = set()
    while s:
        one = s.pop()

        if stack and stack[-1] != one:
            st.add(stack[-1])
        if one in st:
            f = False
            break
        stack.append(one)

    if f:
        ans += 1


print(ans)
