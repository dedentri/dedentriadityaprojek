#-------------------------------LIBRARY-----------------------------------
import streamlit as st 
from pymysql import connect
import streamlit_authenticator as stauth

#-------------------------------DATABASE & LOGIN-----------------------------------
# Gantilah nilai 'host', 'database', 'user', dan 'password' dengan informasi RDS MySQL Anda
db_connection = connect(
    host='localhost',      # Masukkan endpoint RDS Anda di sini
    database='latihan',          # Nama database RDS
    user='root',                # Nama pengguna RDS
    password='dedentriak'    # Password RDS
)
db_cursor = db_connection.cursor()

def authenticate(username, password):
    query = "SELECT * FROM tblogindeden WHERE user=%s AND passwd=%s"
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


# Fungsi untuk menampilkan halaman dashboard
def dashboard_page():
    st.markdown("<h3 style='text-align: center;'>Dashboard</h3>", unsafe_allow_html=True)
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image(st.session_state['gambar'], caption=f"{st.session_state['username']}'s Profile Picture", width=200)
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
        st.rerun()
    
    st.write("------------------------------------------------------------------------------")
    st.write("Apa yang ingin anda ketahui tentang kami?")
    tanya = st.selectbox('Select', ["Siapa Kepala Sekolah SMK Ngeri 1 Banyumas",
                                    "Apa saja jurusan yang ada di SMK Negeri 1 Banyumas",
                                    "Apa yang di pelajari di jurusan TJKT",
                                    "Apa kepanjangan TJKT",
                                    "Sudah berapa lama SMK N 1 Banyumas Berdiri",
                                    "Apa saja organisasi yang ada di SMK Negeri 1 Banyumas"])
    if tanya == "Apa kepanjangan TJKT":
        st.write("TEKNIK JARINGAN KOMPUTER DAN TELEKOMUNIKASI")
    else:
        st.write("Saya Tidak Tahu")

#-------------------------------AUTENTIKASI-----------------------------------
# Memastikan st.session_state['logged_in'] ada saat aplikasi pertama kali dijalankan
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
            st.rerun()  # Refresh page to display dashboard
        else:
            st.error("Username atau password salah.")
else:
    # Tampilkan halaman dashboard jika sudah login
    dashboard_page()

# Menutup koneksi database saat aplikasi selesai dijalankan
db_connection.close()