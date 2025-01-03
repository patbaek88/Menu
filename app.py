import numpy as np
import pandas as pd
import streamlit as st

# 데이터 로드 및 전처리
df = pd.read_csv("Food.csv", encoding="euc-kr")
st.write("데이터 미리보기")
st.dataframe(df)

price_min = st.slider('최소 가격', 0, 100000, 0)
price_max = st.slider('최대 가격', 1000, 1000000, 10000)
delivery = st.checkbox('배달음식')
hunger = st.checkbox('배고픔')
materials = ['돼지','소', '닭', '새우', '골뱅이','생선', '조개', '밀가루', '김치', '감자']
main_material = st.multiselect('주재료', materials, default = materials)
spicy = st.checkbox('매콤')
sweet = st.checkbox('달달')
salty = st.checkbox('짭잘')
oily = st.checkbox('기름진')
time_max = st.slider('최대 소요시간', 5,120, 30)
prefer = st.radio('선호자', ['까치', '물개', '균형'])

filtered_df = df[(df["1인가격"] >= price_min) & (df["1인가격"] <= price_max) & (df["배달가능여부"] == (1 if delivery else 0)) & (df["배고플때"] == (1 if hunger else 0)) & (df["배달가능여부"] == (1 if delivery else 0)) & (df["주재료"].apply(lambda x: any(material in x for material in main_material))) & (df["매콤"] == (1 if spicy else 0)) & (df["달달"] == (1 if sweet else 0)) & (df["짭잘"] == (1 if delivery else 0)) & (df["기름진"] == (1 if oily else 0)) & (df["필요시간"] <= time_max) &(df["선호자"] == prefer)]

st.write("조건에 맞는 메뉴")
st.write(filtered_df["메뉴"].tolist())


