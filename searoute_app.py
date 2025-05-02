import streamlit as st
import requests

# ✅ Kakao 테스트앱 REST API 키 (비공개 저장 권장)
KAKAO_REST_KEY = "6314296c4a7073b3a823df84a30eeab5"

# 📍 주소 → 좌표 변환 함수
def get_coords(address):
    address_fallbacks = {
        "세종시청": "세종특별자치시 도움5로 10",
        "세종특별자치시청": "세종특별자치시 도움5로 10",
        "속초시청": "강원도 속초시 중앙로 183",
        "서울시청": "서울특별시 중구 세종대로 110",
    }
    address = address_fallbacks.get(address.strip(), address.strip())

    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_REST_KEY}"}
    params = {"query": address}
    res = requests.get(url, headers=headers, params=params).json()

    if res.get("documents") and len(res["documents"]) > 0:
        x = res["documents"][0]["x"]
        y = res["documents"][0]["y"]
        return float(x), float(y)
    else:
        st.error(f"❌ 주소 '{address}'에 대한 좌표를 찾을 수 없습니다.")
        return None

# 🚗 Kakao 길찾기 API → 경로 좌표 리스트
def get_route(origin, destination):
    url = "https://apis-navi.kakaomobility.com/v1/directions"
    headers = {"Authorization": f"KakaoAK {KAKAO_REST_KEY}"}
    params = {
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "priority": "RECOMMEND",
    }
    res = requests.get(url, headers=headers, params=params).json()

    if "routes" in res:
        coords = res["routes"][0]["sections"][0]["roads"]
        points = [(p["vertexes"][i], p["vertexes"][i + 1]) for p in coords for i in range(0, len(p["vertexes"]), 2)]
        return points
    else:
        st.error("❌ 경로 데이터를 불러오지 못했습니다.")
        return []

# 🌊 Streamlit 앱 구성
st.set_page_config(page_title="해안도로 경로 추천", page_icon="🌊")
st.title("🌊 바다따라 – 해안도로 감성 경로 추천 앱")

# 입력창
start = st.text_input("출발지 (예: 세종시청)", value="세종시청")
end = st.text_input("도착지 (예: 속초시청)", value="속초시청")

# 버튼 실행
if st.button("경로 추천 받기"):
    st.success(f"출발지: {start} → 도착지: {end}")
    origin = get_coords(start)
    dest = get_coords(end)

    if origin and dest:
        route = get_route(origin, dest)
        if route:
            st.info(f"📍 총 {len(route)}개 지점으로 구성된 경로를 지도에 표시합니다.")
            st.map(data={"lat": [pt[1] for pt in route], "lon": [pt[0] for pt in route]})
