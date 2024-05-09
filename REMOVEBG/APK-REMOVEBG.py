import streamlit as st
from io import BytesIO
from PIL import Image
import io
import rembg
import numpy as np
import base64
import time 
import cv2

st.set_page_config(
    page_title="RemoveApps",
    page_icon="📷",
    initial_sidebar_state="expanded"
)
st.sidebar.markdown("<h3 style = 'text-align: center; font-style: italic;'>Version 2.1 Beta Test</h3>", unsafe_allow_html=True)
st.sidebar.image('Logo.jpg')
st.sidebar.header("Aplikasi Remove Backgorund", divider= 'rainbow')
with st.sidebar:
    with st.spinner("Loading..."):
        time.sleep(3)
    st.success("Status Berhasil!")
    


st.markdown("<h1 class='title' style = 'text-align: center;'>SELAMAT DATANG DI APLIKASI REMOVE BACKGROUND</h1>", unsafe_allow_html=True)
menu = st.sidebar.selectbox('Pilih Opsi', ["Hapus Latar Belakang","Ubah Warna Background","Ubah menjadi hitam putih"])
st.sidebar.markdown("<h4 style = 'text-align: center; font-style: bold;'>Dibuat Oleh Junior Data Science</h4>", unsafe_allow_html=True)

if menu == "Hapus Latar Belakang":
    img = st.file_uploader('Silahkan Upload File Anda')
    if img:
        image = Image.open(io.BytesIO(img.read()))
        st.image(image, caption='Gambar yang akan di edit')
        klik = st.button('HAPUS LATAR BELAKANG')
        if klik:
            input_image = Image.open(img)
            input_array = np.array(input_image)
            output_array = rembg.remove(input_array)
            output_image = Image.fromarray(output_array)
            st.image(output_image, caption="Gambar yang telah di edit")
            
if menu == "Ubah Warna Background":
    img = st.file_uploader('Silahkan Upload File Anda')
    pilih = st.selectbox('Pilih Warna Latar Belakang', ["Merah","Biru","Kuning","Putih","Orange"])
    if img is not None and pilih == "Merah":
        input_image = Image.open(img)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)

        # Buka gambar
        image = output_image

        # Konversi ke mode RGBA (jika tidak sudah)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Ukuran gambar
        width, height = image.size

        # Buat gambar latar belakang baru dengan warna yang diinginkan
        background = Image.new("RGBA", (width, height), (255, 0, 0, 255)) 

        # Gabungkan gambar asli dengan latar belakang
        merged_image = Image.alpha_composite(background, image)
        st.image(input_image, caption="Gambar yang belum di edit")
        st.image(merged_image, caption="Gambar yang telah di edit")
    if img is not None and pilih == "Biru":
        input_image = Image.open(img)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)

        # Buka gambar
        image = output_image

        # Konversi ke mode RGBA (jika tidak sudah)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Ukuran gambar
        width, height = image.size

        # Buat gambar latar belakang baru dengan warna yang diinginkan
        background = Image.new("RGBA", (width, height), (0, 0, 255, 255)) 

        # Gabungkan gambar asli dengan latar belakang
        merged_image = Image.alpha_composite(background, image)
        st.image(input_image, caption="Gambar yang belum di edit")
        st.image(merged_image, caption="Gambar yang telah di edit")
        
    if img is not None and pilih == "Kuning":
        input_image = Image.open(img)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)

        # Buka gambar
        image = output_image

        # Konversi ke mode RGBA (jika tidak sudah)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Ukuran gambar
        width, height = image.size

        # Buat gambar latar belakang baru dengan warna yang diinginkan
        background = Image.new("RGBA", (width, height), (255, 255, 0, 255)) 

        # Gabungkan gambar asli dengan latar belakang
        merged_image = Image.alpha_composite(background, image)
        st.image(input_image, caption="Gambar yang belum di edit")
        st.image(merged_image, caption="Gambar yang telah di edit")

    if img is not None and pilih == "Putih":
        input_image = Image.open(img)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)

        # Buka gambar
        image = output_image

        # Konversi ke mode RGBA (jika tidak sudah)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Ukuran gambar
        width, height = image.size

        # Buat gambar latar belakang baru dengan warna yang diinginkan
        background = Image.new("RGBA", (width, height), (255, 255, 255, 255)) 

        # Gabungkan gambar asli dengan latar belakang
        merged_image = Image.alpha_composite(background, image)
        st.image(input_image, caption="Gambar yang belum di edit")
        st.image(merged_image, caption="Gambar yang telah di edit")
        
    if img is not None and pilih == "Orange":
        input_image = Image.open(img)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)

        # Buka gambar
        image = output_image

        # Konversi ke mode RGBA (jika tidak sudah)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Ukuran gambar
        width, height = image.size

        # Buat gambar latar belakang baru dengan warna yang diinginkan
        background = Image.new("RGBA", (width, height), (255, 165, 0, 255)) 

        # Gabungkan gambar asli dengan latar belakang
        merged_image = Image.alpha_composite(background, image)
        st.image(input_image, caption="Gambar yang belum di edit")
        st.image(merged_image, caption="Gambar yang telah di edit")
        
if menu == "Ubah menjadi hitam putih":
    img = st.file_uploader('Silahkan Upload File Anda')
    if img: 
        color_image = Image.open(img)
        bw = color_image.convert('L')
        st.image(color_image, caption="Gambar yang belum di edit")
        st.image(bw, caption="Gambar yang telah di edit")