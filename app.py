import streamlit as st
import pandas as pd

df = pd.read_csv("第1表.csv", header=[0,1],)

st.header('食中毒の原因食品と発生')

with st.sidebar:
    prefecture = st.multiselect('地域を選択してください',
                                    df[df.columns[0]])
    prime_category = st.radio('')

#with st.sidebar:
if prefecture == []:
    st.subheader('食中毒の原因食品と発生の詳細の表')
    df.set_index('地域', inplace=True)
    st.dataframe(
        df , width=800, height=500
    )    
else:
    df = df[df[df.columns[0]].isin(prefecture)]
    df.set_index('地域', inplace=True)
    st.dataframe(df, width=800)