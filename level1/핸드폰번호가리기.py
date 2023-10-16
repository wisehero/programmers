def solution(phone_number):
    front = "*" * len(phone_number[:-4])
    back = phone_number[-4:]
    return front + back
