try:
    import jeju_region as rg
    import course_recommendation as cr

except ModuleNotFoundError:
    print("실행에 필요한 모듈이 설치되어 있지 않습니다. pandas, random, geopy 모듈을 설치한 후 실행해주세요.")
    exit(0) # 모듈 오류 메시지 출력 후 프로그램 즉시 종료

# 사용자가 권역을 선택하고 출발지를 입력함
try:

    while True:
        print("========== 제주도 여행 코스 추천 프로그램 ==========")
        print("1. 제주시  2. 제주서부  3. 서귀포시  4. 제주동부")
        print("5. 권역의 세부 지역 정보 설명")
        region_num = int(input("여행을 원하는 권역의 번호를 선택하세요. -> "))

        # 선택한 번호에 맞게 코스 추천 메시지 출력
        if region_num == 1:
            print("\n제주시의 여행 코스를 추천해드릴게요.\n")
            cr.CourseRecommend(region_num) # 코스 추천 함수 호출
            break
        elif region_num == 2:
            print("\n제주서부의 여행 코스를 추천해드릴게요.\n")
            cr.CourseRecommend(region_num) # 코스 추천 함수 호출
            break
        elif region_num == 3:
            print("\n서귀포시의 여행 코스를 추천해드릴게요.\n")
            cr.CourseRecommend(region_num) # 코스 추천 함수 호출
            break
        elif region_num == 4:
            print("\n제주동부의 여행 코스를 추천해드릴게요.\n")
            cr.CourseRecommend(region_num) # 코스 추천 함수 호출
            break
        
        # 세부 지역 정보 표시하기(각 권역 별 동 정보)
        elif region_num == 5:
            region_info = int(input("어느 권역의 세부 지역 정보가 필요하신가요?(숫자 입력) "))
            print()
            if region_info == 1:
                print("1. 제주시 권역의 세부 지역 정보는 다음과 같습니다.")
                print(rg.jeju1, "\n")
                continue
            elif region_info == 2:
                print("2. 제주서부 권역의 세부 지역 정보는 다음과 같습니다.")
                print(rg.jeju2, "\n")
                continue
            elif region_info == 3:
                print("3. 서귀포시 권역의 세부 지역 정보는 다음과 같습니다.")
                print(rg.jeju3, "\n")
                continue
            elif region_info == 4:
                print("4. 제주동부 권역의 세부 지역 정보는 다음과 같습니다.")
                print(rg.jeju4, "\n")
                continue
            else:
                print("올바른 권역 번호를 입력해주세요.\n")
        # 잘못된 권역 번호 입력 시
        else:
            print("올바른 권역 번호를 입력해주세요.")
            continue

# 오류 발생 시 예외처리
# 파일을 찾을 수 없는 경우 예외처리
except FileNotFoundError:
    print("실행에 필요한 장소 csv 파일이 존재하지 않습니다. 파일을 올바른 경로에 위치시킨 후 실행해주세요.")

# 그외 모든 오류 예외처리
except:
    print("오류가 발생했습니다. 모듈 설치 여부나 파일 존재 여부 등을 확인해주세요.")
