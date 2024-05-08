import streamlit as st
import pandas as pd
import joblib 
model = joblib.load("Model-Pizza-XGB.pkl")

st.title("APLIKASI PREDIKSI HARGA PIZZA")
st.text('Perusahaan: 0 = Pizza Banyumasan')
st.text('Perusahaan: 1 = Pizza Sahara')        
st.text('Perusahaan: 2 = Pizza Desa')        
st.text('Perusahaan: 4 = Pizza Modern')        

perusahaan = st.selectbox('Perusahaan', [0,1,2,3,4])
diameter = st.number_input('pilih diameter')
topping = st.selectbox('Topping', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
variant = st.selectbox('Varian', [0,1,2,3,4,5,6,7,8,9,10])
ukuran = st.selectbox('Ukuran', [0,1,2,3,4,5])
saus = st.radio('Extra Sauce:', [0,1])
keju = st.radio('Extra Chesse:', [0,1])
jamur = st.radio('Extra Mushrooms:', [0,1])

tombol = st.button('Prediksi')

if tombol:
    input_data = pd.DataFrame({'perusahaan':[perusahaan],
            'diameter':[diameter],
            'topping':[topping],
            'variant':[variant],
            'ukuran':[ukuran],
            'extra_sauce':[saus],
            'extra_cheese':[keju],
            'extra_mushrooms':[jamur]
})
    df = st.dataframe(input_data)
    prediksi = model.predict(input_data)
    st.success(f"Prediksi Harga Pizza Adalah Rp {prediksi[0]}")

