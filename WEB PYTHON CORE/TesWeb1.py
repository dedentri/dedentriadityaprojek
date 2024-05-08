#JALANKAN DENGAN CARA OPEN CMD DAN KETIK "streamlit run TesWeb1.py"
import streamlit as st

st.write("""
#APLIKASI KALKULATOR SEDERHANA UNTUK UJI COBA""")

angka1 = st.number_input("Masukan angka pertamamu: ", 0)
angka2 = st.number_input("Masukan angka keduamu: ", 0)
pilih = st.selectbox('Plih Operasi', ["kali","bagi","kurangi","tambah","pangkat"])
hitung = st.button("Jumlah")

if hitung:
    if pilih == "kali":
        st.success(f"Hasilnya adalah {angka1 * angka2}")
        st.balloons()
    elif pilih == "bagi":
        st.success(f"Hasilnya adalah {angka1 / angka2}")
        st.balloons()
    elif pilih == "kurangi":
        st.success(f"Hasilnya adalah {angka1 - angka2}")
        st.balloons()
    elif pilih == "tambah":
        st.success(f"Hasilnya adalah {angka1 + angka2}")
        st.balloons()
    elif pilih == "pangkat":
        st.success(f"Hasilnya adalah {angka1 ** angka2}")
        st.balloons()
