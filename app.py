import streamlit as st
st.set_page_config(
    layout="wide",                
)
import pandas as pd

df = pd.read_csv("file.csv", header=[0,1],)
category = df.iloc[0].unique()

st.header('食中毒の原因食品と地域ごとの比較')

with st.sidebar:
    prefecture = st.multiselect('地域を選択してください',
                                    df[df.columns[0]])
    prime_category = st.multiselect('カテゴリーを選択してください', df.columns.get_level_values(0).unique()[1:])
    with st.expander('出典'):
        ('https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00450191&tstat=000001040259&file_type=1&result_page=1&metadata=1&data=1, 2026/2/2取得)')


st.subheader('サイドバーで地域、カテゴリーの選択をし、食中毒と地域ごとの発生回数を知り、比較することができるアプリです')
st.subheader('食中毒の原因食品と発生地域の表')
if prefecture == []:
    df.set_index('地域', inplace=True)
    if prime_category != []:
        df = df[prime_category]
        st.toast('情報が更新されました')
    st.dataframe(
        df , height=500
    )    
else:
    st.toast('情報が更新されました')
    df = df[df[df.columns[0]].isin(prefecture)]
    df.set_index('地域', inplace=True)
    if prime_category != []:
        df = df[prime_category]
    st.dataframe(df)



