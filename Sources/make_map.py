# 라이브러리 불러오기
import requests
import pandas as pd
import numpy as np
import folium # 지도 시각화 라이브러리
from folium.plugins import MiniMap

# 지도를 표출하는 함수
def make_map(dfs):
    # 기준지 - 제주국제공항
    m = folium.Map(location=[33.5101562, 126.4861157], zoom_start=12)
    # 미니맵 추가
    minimap = MiniMap()
    m.add_child(minimap)
    # 마커 추가
    for i in range(len(dfs)):
        folium.Marker([dfs['y'][i], dfs['x'][i]],
                      tooltip=dfs['stores'][i],
                      popup=dfs['place_url'][i],).add_to(m)
    return m 