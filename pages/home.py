import streamlit as st
import pandas as pd

def next_page():
    st.switch_page("pages/normalization.py")

if 'dataset' not in st.session_state:
    st.session_state['dataset'] = 'value'

st.title("Input Data Saham")
selected_stock = st.selectbox("Nama Saham", ("BBCA", "ANTM", "INDF", "UNVR"))
st.text_input("File Data Saham",value=f"{selected_stock}.csv", disabled=True)

st.session_state['dataset'] = selected_stock

dataset_path = f"dataset/{selected_stock}.csv"
'''
'''
df = pd.read_csv(dataset_path,parse_dates=['Date'], index_col=['Date'])
df = df.sort_index()
st.dataframe(df.head(), width=750)
df.columns = df.columns.str.strip()
st.line_chart(df['Close'])

c1, c2, c3, c4, c5, c6 = st.columns(6, gap="large")
c6.button(label="Next", on_click=next_page)
