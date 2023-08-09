import sys

m, n, k = map(int, input().split(" "))

secret = "".join(input().split(" "))
user_input = "".join(input().split(" "))

if secret in user_input:
    print("secret")
else:
    print("normal")

