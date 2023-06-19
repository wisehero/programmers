def solution(chicken):
    answer = 0
    coupon = chicken

    service = 0

    while True:
        service = coupon // 10
        coupon -= service * 10
        coupon += service
        answer += service

        if coupon < 10:
            break

    return answer