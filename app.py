import streamlit as st
import pandas as pd

# 웹페이지 전체 넓게 쓰기
st.set_page_config(layout="wide")

# 대시보드 제목
st.title("교통문제 해결을 위한 데이터 분석 결과 🚦")
st.write("분석이 완료된 4가지 결과 데이터입니다. 아래 표에서 항목을 클릭하거나 스크롤하여 데이터를 확인할 수 있습니다.")

# 1. 승하차구역 목록
st.subheader("1. 승하차구역 목록")
df1 = pd.read_csv("결과_승하차구역_목록.csv")
st.dataframe(df1, use_container_width=True)

# 2. 우선순위지수
st.subheader("2. 우선순위지수")
df2 = pd.read_csv("결과_우선순위지수.csv")
st.dataframe(df2, use_container_width=True)

# 3. 자치구별 현황
st.subheader("3. 자치구별 현황")
df3 = pd.read_csv("결과_자치구별_현황.csv")
st.dataframe(df3, use_container_width=True)

# 4. 학교별 관리공백
st.subheader("4. 학교별 관리공백")
df4 = pd.read_csv("결과_학교별_관리공백.csv")
st.dataframe(df4, use_container_width=True)
