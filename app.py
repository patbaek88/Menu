import numpy as np
import pandas as pd
import streamlit as st

# 데이터 로드 및 전처리
df = pd.read_csv("Food.csv", encoding="euc-kr")
st.write("데이터 미리보기")
st.dataframe(df)

price_min = st.slider('최소 가격', 0, 100000, 0)
price_max = st.slider('최대 가격', 1000, 100000, 20000)
delivery = st.checkbox('배달음식')
hunger = st.checkbox('배고픔')
materials = ['pork','beef', 'chicken', 'shrimp', 'golbaengi','fish', 'clam', 'flower', 'kimchi', 'potato']
main_material = st.multiselect('주재료', materials, default = materials)
spicy = st.checkbox('매콤')
sweet = st.checkbox('달달')
salty = st.checkbox('짭잘')
oily = st.checkbox('기름진')
time_max = st.slider('최대 소요시간', 5,120, 30)
prefer = st.radio('선호자', ['Jaeuk', 'Heeeun', 'both'])

filtered_df = df[(df["unit price"] >= price_min) & (df["unit price"] <= price_max) & (df["delivery"] == (1 if delivery else 0)) & (df["hungry"] == (1 if hunger else 0)) & (df["delivery"] == (1 if delivery else 0)) & (df["main ingredient"].apply(lambda x: any(material in x for material in main_material))) & (df["spicy"] >= (1 if spicy else 0)) & (df["sweet"] >= (1 if sweet else 0)) & (df["salty"] >= (1 if salty else 0)) & (df["oily"] >= (1 if oily else 0)) & (df["time"] <= time_max) &(df["prefer"] == prefer)]

st.write("조건에 맞는 메뉴")
st.write(filtered_df["menu"].tolist())


