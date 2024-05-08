#JALANKAN DENGAN CARA OPEN CMD DAN KETIK "streamlit run TesWeb2.py"
import streamlit as st

st.write("""
#APLIKASI KALKULATOR BMI SEDERHANA UNTUK UJI COBA""")

berat_badan = st.number_input("Masukan berat badanmu: ", 0)
tinggi_badan = st.number_input("Masukan tinggi badan mu: ", 0)
hitung = st.button("Jalankan")

if hitung:
    hasil=berat_badan/(tinggi_badan/100)**2
    st.write(f"Hasil BMI adalah {hasil}")
    if hasil < 18: #JIKA HASILNYA DI BAWAH 18 MAKA BERAT BADAN KURANG 
        st.write('berat badan kamu kurang')
    elif hasil < 22.9:  #JIKA HASILNYA DI BAWAH 22,9 MAKA BERAT BADAN NORMAL 
        st.success('berat badan kamu normal')
    elif hasil == 23:  #JIKA HASILNYA SAMA DENGAN 23 MAKA BERAT BADAN BERLEBIHAN 
        st.warning('berat badan kamu berlebihan')
    elif hasil <= 24:  #JIKA HASILNYA KURANG/SAMA DENGAN 24 MAKA BERAT BADAN TERLALU BERLEBIHAN 
        st.warning('berat badan kamu terlalu berlebihan')
    elif hasil <= 29.9: #JIKA HASILNYA KURANG/SAMA DENGAN 29,9 MAKA BERAT BADAN MENGALAMI OBESITAS TAHAP 1
        st.warning('obesitas tahap 1')
    else:#OPSI TERAKHIR JIKA RUMUS MENGHASILKAN ANGKA DI ATAS 29,9 MAKA TERMASUK OBESITAS TAHAM 2 YANG BERBAHAYA
        st.warning('obesitas tahap 2,bahaya!!!')