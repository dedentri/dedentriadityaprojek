#-------------------------------LIBRARY-----------------------------------
import streamlit as st 
from pymysql import connect
import streamlit_authenticator as stauth
import pandas as pd

import time
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

#-------------------------------DATABASE & LOGIN-----------------------------------
db_connection = connect(host='localhost', database='latihan', user='root', password='dedentriak')
db_cursor = db_connection.cursor()

def authenticate(username, password):
    query = "SELECT * FROM users WHERE user=%s AND passwd=%s"
    db_cursor.execute(query, (username, password))
    result = db_cursor.fetchone()
    if result:
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
        st.session_state['gambar'] = result[3]
        st.session_state['gmail'] = result[4]
        st.session_state['nomor'] = result[5]
        st.session_state['gender'] = result[6]
        st.session_state['country'] = result[7]
        st.session_state['region'] = result[8]
        st.session_state['birth'] = result[9]
        st.session_state['job'] = result[10]
    return result is not None

# Membaca dataset dari file CSV
df = pd.read_csv("Chatbot_asean.csv")

# Memisahkan dataset menjadi data pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(df['Pertanyaan'], df['Intent'], test_size=0.2, random_state=42)

# Fungsi untuk melakukan vektorisasi teks
def vectorize_text(X_train, X_test):
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    return X_train_vec, X_test_vec, vectorizer

# Melatih model klasifikasi SVM
def train_model(X_train_vec, y_train):
    model = LinearSVC()
    model.fit(X_train_vec, y_train)
    return model

# Evaluasi model
def evaluate_model(model, X_test_vec, y_test):
    y_pred = model.predict(X_test_vec)
    report = classification_report(y_test, y_pred)
    return report, y_pred

# Vektorisasi data teks
X_train_vec, X_test_vec, vectorizer = vectorize_text(X_train, X_test)

# Melatih model dengan data pelatihan
model = train_model(X_train_vec, y_train)

def print_typing_effect(text, delay=0.01):
    # Menggunakan st.empty() untuk membuat placeholder teks
    typing_placeholder = st.empty()

    typing_text = ""
    for char in text:
        typing_text += char
        typing_placeholder.markdown(typing_text)  # Memperbarui teks secara dinamis
        time.sleep(delay)

# Fungsi untuk menampilkan halaman dashboard
def dashboard_page():
    st.markdown("<h3 style='text-align: center;'>Dashboard</h3>", unsafe_allow_html=True)
#    left_co, cent_co, last_co = st.columns(3)
#    with cent_co:
#        st.image(st.session_state['gambar'], caption=f"{st.session_state['username']}'s Profile Picture", width=200)
    st.write("------------------------------------------------------------------------------")
    st.write(f"Alamat Gmail Yang Terkait: {st.session_state['gmail']}")
    st.write(f"Nomor Yang Terkait: {st.session_state['nomor']}")
    st.write(f"Gender: {st.session_state['gender']}")
    st.write(f"Country: {st.session_state['country']}")
    st.write(f"Region: {st.session_state['region']}")
    st.write(f"Birth: {st.session_state['birth']}")
    st.write(f"Job: {st.session_state['job']}")
    
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()
    
    st.write("------------------------------------------------------------------------------")
    st.write("Apa yang ingin anda tanyakan?")
    tanya = st.text_input("MASUKAN PERTANYAAN ANDA")
    if tanya:
        user_input_vec = vectorizer.transform([tanya.lower()])
        predicted_intent = model.predict(user_input_vec)[0]
        if predicted_intent in df['Pertanyaan'].values:
            response = df[df['Pertanyaan'] == predicted_intent]['Jawaban'].values[0]
            print_typing_effect(tanya)
            print_typing_effect(response)
    

#-------------------------------AUTENTIKASI-----------------------------------
# Memastikan `st.session_state['logged_in']` ada saat aplikasi pertama kali dijalankan
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Halaman login
if not st.session_state['logged_in']:
    placeholder = st.empty()
    with placeholder.form("login"):
        st.markdown("<h3 style='text-align: center;'>Silahkan Login</h3>", unsafe_allow_html=True)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if authenticate(username, password):
            st.success(f"Login berhasil! Selamat datang {username}")
            placeholder.empty()
            st.experimental_rerun()  # Refresh page to display dashboard
        else:
            st.error("Username atau password salah.")
else:
    # Tampilkan halaman dashboard jika sudah login
    dashboard_page()

# Menutup koneksi database saat aplikasi selesai dijalankan
db_connection.close()
