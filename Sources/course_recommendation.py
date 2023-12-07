import pandas as pd
import random

# csv파일 읽는 함수
def read_file(filename):
    df = pd.read_csv(filename, encoding='cp949')
    return df

# 여행 코스를 추천해주는 함수
def CourseRecommend(region, files):
    courses = []
    
    for idx, file in enumerate(files):
        df = read_file(file)
        if 'stores' in df.columns:
            place_list = df['stores'].tolist()
            
            # 파일순으로 하나씩 선택
            selected_place = random.choice(place_list)
            courses.append(selected_place)
    
    print("======== 여행 코스 추천 ========")
    print(f"선택하신 {region}구역의 여행 코스를 랜덤으로 추천해 드립니다.")
    for i, place in enumerate(courses, start=1):
        if i == 1:
            print(f"{i}.관광지 - {place}")
        elif i == 2:
            print(f"{i}.카페 및 기념품 - {place}")
        elif i == 3:
            print(f"{i}.음식점 - {place}")



if __name__ == "__main__":
    file_paths = ["jeju1_tour_region.csv",
              "jeju1_cafe_souvenir.csv",
              "jeju1_restaurant.csv"]
    
    CourseRecommend(1, file_paths)

