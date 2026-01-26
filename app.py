import streamlit as st
import pandas as pd

df1 = pd.read_csv("第1表.csv")
df2 = pd.read_csv("第2表.csv")
df3 = pd.read_csv("第3表.csv")

with st.sidebar:
    options = ["原因食品", "病因物質", "原因施設"]
    select = st.segmented_control(
        "カテゴリの選択", options, selection_mode="single",
    )
    prefecture = st.multiselect('都道府県を選択してください',
                                    df1['都道府県'])

if select == "原因食品":
    #with st.sidebar:
    if prefecture == []:
        st.dataframe(df1, width=800, height=500)    
    else:
        df1 = df1[df1['都道府県'].isin(prefecture)]
        df1.set_index('都道府県', inplace=True)
        st.dataframe(df1, width=800)