import pandas as pd
import random

# csv파일 읽는 함수
def read_file(filename):
    df = pd.read_csv(filename, encoding='cp949')
    return df

# 여행 코스를 추천해주는 함수
def CourseRecommend(region):
    # 구역 번호에 맞는 구역 장소 파일 이름을 저장함
    if region == 1:
        files =  ["jeju1_tour_region.csv",
                  "jeju1_cafe_souvenir.csv",
                  "jeju1_restaurant.csv"]
    elif region == 2:
        files =  ["jeju2_tour_region.csv",
                  "jeju2_cafe_souvenir.csv",
                  "jeju2_restaurant.csv"]
    elif region == 3:
        files =  ["jeju3_tour_region.csv",
                  "jeju3_cafe_souvenir.csv",
                  "jeju3_restaurant.csv"]
    elif region == 4:
        files =  ["jeju4_tour_region.csv",
                  "jeju4_cafe_souvenir.csv",
                  "jeju4_restaurant.csv"]
    
    courses = []
    
    for idx, file in enumerate(files):
        df = read_file(file)
        if 'stores' in df.columns:
            place_list = df['stores'].tolist() # 장소명 리스트
            url_list = df['place_url'].tolist()  # 장소 url 가져와서 리스트에 저장
            
            # 파일순으로 하나씩 선택
            selected_index = random.choice(range(len(place_list)))
            selected_place = place_list[selected_index]
            selected_url = url_list[selected_index] if 'place_url' in df.columns else "url 없음"
            
            # 장소와 url을 저장
            courses.append((selected_place, selected_url))
    
    print("================ 여행 코스 추천 ================")
    print(f"선택하신 {region}구역의 여행 코스를 랜덤으로 추천해 드립니다.")
    
    # 징소를 랜덤으로 추천해주고 장소의 url도 함께 출력함
    for i, (place, url) in enumerate(courses, start=1):
        if i == 1:
            print(f"{i}.관광지 - {place} ({url})")
        elif i == 2:
            print(f"{i}.카페 및 기념품 - {place} ({url})")
        elif i == 3:
            print(f"{i}.음식점 - {place} ({url})")
            print()
    ContinueRecommend(region)

# 코스를 계속 추천받을지 입력받는 함수
def ContinueRecommend(region_num):
    while True:
        diff_course = input("다른 코스를 추천받으시겠어요? (Y / N(종료)) ")
        print()
        # y 입력 시 새로운 코스 추천
        if diff_course.lower() == "y":
            CourseRecommend(region_num)
        # n 입력 시 프로그램을 종료함
        elif diff_course.lower() == "n":
            print("여행 코스 추천 프로그램을 종료합니다.")
            break
        # 다른 문자 입력 시 문자를 재입력받음
        else:
            print("올바른 문자를 입력해주세요.")
            continue
        break

# 코드 테스트
if __name__ == "__main__":
    CourseRecommend(1) # 1구역
