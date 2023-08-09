import sys

car_a, car_b = map(int, sys.stdin.readline().split())

if car_a > car_b:
    print("A")
elif car_b > car_a:
    print("B")
else:
    print("same")