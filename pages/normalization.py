from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import pandas as pd

st.title("Normalisasi Data Saham")

dataset = st.session_state['dataset']
dataset_path = f"dataset/{dataset}.csv"
df = pd.read_csv(dataset_path, parse_dates=['Date'], index_col=['Date'])

c1, c2 = st.columns(2)
with c1:
    st.write("Nama Saham:")
    st.write("Jumlah Data:")
with c2:
    st.write(dataset)
    st.write(str(df.size))

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns, index=df.index)
st.dataframe(scaled_df.head(), width=750)