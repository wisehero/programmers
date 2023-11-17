import sys
from collections import deque

t = int(sys.stdin.readline())
q = deque()

while t:
    command = sys.stdin.readline().rstrip()

    if command == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif command == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    elif command == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif command == "size":
        print(len(q))
    else:
        c, n = command.split(" ")
        if c == "push_back":
            q.append(n)
        else:
            q.appendleft(n)

    t -= 1
