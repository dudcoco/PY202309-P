import pandas as pd
import random
from geopy.distance import geodesic

# csv파일 읽는 함수
def read_file(filename):
    df = pd.read_csv(filename, encoding='cp949')
    return df

# 위도 경도를 이용하여 두 지점 간의 거리를 계산하는 함수
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).km

# 여행 코스를 추천해주는 함수
def CourseRecommend(region):
    # 구역 번호에 맞는 구역 장소 파일 이름을 저장함
    if region == 1:
        files = ["jeju1_tour_region.csv",
                 "jeju1_cafe_souvenir.csv",
                 "jeju1_restaurant.csv"]
    elif region == 2:
        files = ["jeju2_tour_region.csv",
                 "jeju2_cafe_souvenir.csv",
                 "jeju2_restaurant.csv"]
    elif region == 3:
        files = ["jeju3_tour_region.csv",
                 "jeju3_cafe_souvenir.csv",
                 "jeju3_restaurant.csv"]
    elif region == 4:
        files = ["jeju4_tour_region.csv",
                 "jeju4_cafe_souvenir.csv",
                 "jeju4_restaurant.csv"]

    courses = {"관광지": {"data": []},
               "카페 및 기념품": {"data": []},
               "음식점": {"data": []}}

    for idx, file in enumerate(files):
        df = read_file(file)
        if 'x' in df.columns and 'y' in df.columns:
            coord_list = df.apply(lambda row: (row['y'], row['x']), axis=1).tolist()

            # 파일순으로 하나씩 선택
            selected_index = random.randrange(len(coord_list))
            selected_coord = coord_list[selected_index]

            # 관광지 선택
            place = df.loc[selected_index, 'stores']
            url = df.loc[selected_index, 'place_url'] if 'place_url' in df.columns else "url 없음"
            courses["관광지"]["data"].append((place, url))
            print(courses)

            # 카페 및 기념품 선택 (반경 5km 이내, 중복 방지)
            cafe_souvenir_candidates = [i for i, coord in enumerate(coord_list) if
                                        calculate_distance(selected_coord, coord) <= 5 and df.loc[i, 'stores'] not in
                                        [p[0] for p in courses["관광지"]["data"]]]
            selected_cafe_souvenir = random.choice(cafe_souvenir_candidates) if cafe_souvenir_candidates else None
            if selected_cafe_souvenir is not None:
                place = df.loc[selected_cafe_souvenir, 'stores']
                url = df.loc[selected_cafe_souvenir, 'place_url'] if 'place_url' in df.columns else "url 없음"
                courses["카페 및 기념품"]["data"].append((place, url))

                # 음식점 선택 (반경 5km 이내, 중복 방지)
                restaurant_candidates = [i for i, coord in enumerate(coord_list) if
                                         calculate_distance(coord_list[selected_cafe_souvenir], coord) <= 5 and df.loc[
                                             i, 'stores'] not in [p[0] for p in courses["카페 및 기념품"]["data"]]]
                selected_restaurant = random.choice(restaurant_candidates) if restaurant_candidates else None
                if selected_restaurant is not None:
                    place = df.loc[selected_restaurant, 'stores']
                    url = df.loc[selected_restaurant, 'place_url'] if 'place_url' in df.columns else "url 없음"
                    courses["음식점"]["data"].append((place, url))

    print("================ 여행 코스 추천 ================")
    print(f"선택하신 {region}구역의 여행 코스를 랜덤으로 추천해 드립니다.")
    print("(관광지 > 카페 및 기념품 > 음식점 순서로 추천합니다.)\n")

    for category in ["관광지", "카페 및 기념품", "음식점"]:
        for i in range(3):  # 3번 출력
        # for category in ["관광지", "카페 및 기념품", "음식점"]:
            place, url = courses[category]["data"][i]
            print(f"- {category} : {place} ({url})")

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