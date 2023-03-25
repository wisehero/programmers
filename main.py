def solution(chicken):
    answer = 0
    coupon = chicken
    while True:
        service = coupon // 10
        answer += service
        coupon -= service * 10
        coupon += service

        if coupon < 10:
            break

solution(1081)