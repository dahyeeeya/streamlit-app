import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Streamlit Cloud 환경용 맑은 고딕 등)
# 주의: Streamlit Cloud에서는 한글 폰트가 깨질 수 있으므로 운영체제에 맞는 폰트 설정이 필요할 수 있습니다.
# 임시로 나눔고딕을 사용하도록 설정하거나, 폰트 깨짐 방지 코드를 추가해야 할 수 있습니다.
plt.rc('font', family='NanumGothic') 
plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(layout="wide")
st.title("교통문제 해결을 위한 데이터 분석 결과 🚦")

# 데이터 불러오기
df1 = pd.read_csv("결과_승하차구역_목록.csv")
# 나머지 데이터도 필요하다면 불러오기
# df2 = pd.read_csv("결과_우선순위지수.csv")
# df3 = pd.read_csv("결과_자치구별_현황.csv")
# df4 = pd.read_csv("결과_학교별_관리공백.csv")

st.subheader("1. 안심승하차구역 정차구간 길이 분포")

# --- 히스토그램 시각화 (오른쪽 차트) ---
# df1(승하차구역 목록)에 '길이m' 컬럼이 있다고 가정합니다.
fig, ax = plt.subplots(figsize=(8, 5))
# 길이 데이터를 숫자로 변환 (결측치나 'None' 문자열 처리)
df1['길이m'] = pd.to_numeric(df1['길이m'], errors='coerce')
sns.histplot(df1['길이m'].dropna(), bins=10, ax=ax, edgecolor='white')

# 중앙값 점선 그리기 (코랩 사진 기준 12m)
median_length = 12 
ax.axvline(median_length, color='red', linestyle='--', label=f'중앙값 {median_length}m')
ax.set_title("안심승하차구역 정차구간 길이 분포")
ax.set_xlabel("정차구간 길이(m)")
ax.set_ylabel("구간 수")
ax.legend()
ax.grid(alpha=0.3)

# Streamlit에 차트 출력
st.pyplot(fig)

st.divider()

# --- 데이터 표 출력 (원래 있던 것) ---
st.subheader("2. 전체 데이터 확인")
st.dataframe(df1, use_container_width=True)
