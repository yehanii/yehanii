point = 2

def coffee_point(point):
    if point<10:
        print("포인트가 부족합니다.")
        print(f"무료 커피 획득까지 {10-point}잔 남음")
        return point
    else:
        print("커피 포인트 사용이 완료되었습니다.")
        point-= 10
        print("잔여 포인트는 {point}입니다.")
        return point
coffee_point(point)
    