import pandas as pd
import random
from geopy.distance import geodesic

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
    
    courses = {"관광지": [], "카페 및 기념품": [], "음식점": []}
    
    for idx, file in enumerate(files):
        df = read_file(file)
        if 'stores' in df.columns and 'x' in df.columns and 'y' in df.columns:
            place_list = df['stores'].tolist()
            url_list = df['place_url'].tolist()
            coordinates = list(zip(df['y'], df['x']))  # 순서를 바꿔서 가져오기

            selected_indices = random.sample(range(len(place_list)), 2)
            selected_places = [place_list[i] for i in selected_indices]
            selected_urls = [url_list[i] if 'place_url' in df.columns else "url 없음" for i in selected_indices]
            selected_coordinates = [coordinates[i] for i in selected_indices]

            # 기준 장소 선택 (맨 첫번째로 출력될 장소)
            base_place, base_url, base_coord = selected_places[0], selected_urls[0], selected_coordinates[0]

            # 거리 계산하여 정렬
            distances = [geodesic(base_coord, coord).km for coord in selected_coordinates]
            sorted_indices = sorted(range(len(distances)), key=lambda k: distances[k])

            # 카테고리 먼저 선언
            category = "관광지" if idx == 0 else ("카페 및 기념품" if idx == 1 else "음식점")

            # 장소와 url을 저장 (가까운 순으로)
            for i in sorted_indices:
                place, url, coord = selected_places[i], selected_urls[i], selected_coordinates[i]
                courses[category].append((place, url, coord))


    print("================ 여행 코스 추천 ================")
    print(f"선택하신 {region}구역의 여행 코스를 랜덤으로 추천해 드립니다.")
    print("(관광지 > 카페 및 기념품 > 음식점 순서로 추천합니다.)\n")
    
    # 징소를 랜덤으로 추천해주고 장소의 url도 함께 출력함
    for i in range(2):  # 2번 출력
        for category in ["관광지", "카페 및 기념품", "음식점"]:
            place, url, coord = courses[category][i]
            print(f"- {category} : {place} ({url})")


    ContinueRecommend(region)

# 코스를 계속 추천받을지 입력받는 함수
def ContinueRecommend(region_num):
    while True:
        diff_course = input("\n다른 코스를 추천받으시겠어요? (Y / N(종료)) ")
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
    CourseRecommend(1)  # 1구역