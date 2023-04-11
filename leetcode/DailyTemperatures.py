def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for d, t in enumerate(temperatures):
        while stack and stack[-1][1] < t:
            prev_day, _ = stack.pop()
            answer[prev_day] = d - prev_day
        stack.append((d, t))
    return answer
