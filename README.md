# 바다따라 – 해안도로 감성 경로 추천 앱

📍 관광데이터 활용 공모전 출품작  
🛠 현재 개발 중인 비상업용 앱입니다.

## 주요 기능
- Kakao 주소검색 + 길찾기 API 사용
- 출발지~도착지 경로 분석
- 해안선 거리 기반 해안성 점수 계산
- TourAPI로 주변 관광지 표시

## 실행 파일
🔗 [`searoute_app.py`](./searoute_app.py)

이 파일을 실행하면 Streamlit 기반 웹앱이 로컬에서 실행됩니다.

## 실행화면 예시
*스크린샷은 `screenshots/` 폴더에 추가해 주세요*

## 로컬 실행 방법

```bash
git clone https://github.com/rPwjd99/route-app.git
cd route-app
pip install streamlit requests
streamlit run searoute_app.py
