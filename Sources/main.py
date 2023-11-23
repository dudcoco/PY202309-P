import jeju_region as region

# 사용자가 권역을 선택하고 출발지를 입력함
print("====== 제주도 여행 코스 추천 프로그램 ======")
while True:

    print("1. 제주시  2. 제주서부  3. 서귀포시  4. 제주동부")
    user_input = int(input("여행을 원하는 권역의 번호를 선택하세요. -> "))

    if user_input == 1:
        print("제주시의 여행 코스를 추천해드릴게요.")
        break
    elif user_input == 2:
        print("제주서부의 여행 코스를 추천해드릴게요.")
        break
    elif user_input == 3:
        print("서귀포시의 여행 코스를 추천해드릴게요.")
        break
    elif user_input == 4:
        print("제주동부의 여행 코스를 추천해드릴게요.")
        break
    else:
        print("올바른 권역 번호를 입력해주세요.")
        continue

