import streamlit as st

# 1. Cấu hình trang
st.set_page_config(page_title="Quà tặng đặc biệt", page_icon="🐱", layout="centered")

# 2. Khởi tạo trạng thái
if 'step' not in st.session_state:
    st.session_state.step = 'trang_keo_day'

# 3. Giao diện CSS (Sửa lỗi căn giữa, xóa khung trắng, tạo thiệp hình chữ nhật)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&family=Dancing+Script:wght@700&display=swap');
    
    /* Nền trang */
    .stApp { background-color: #fff0f3; overflow: hidden; }

    /* Hiệu ứng hoa rơi */
    .cherry-blossom { position: fixed; top: -10%; z-index: 9999; user-select: none; animation: fall linear infinite; }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); opacity: 1; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0; } }
    
    /* Căn giữa hình ảnh */
    .stImage > img { display: block; margin-left: auto; margin-right: auto; border-radius: 20px; }

    /* Lá thiệp hình chữ nhật cho phần nội dung */
    .the-thiep {
        background: white; 
        padding: 40px; 
        border-radius: 15px; /* Bo góc nhẹ tạo hình chữ nhật xịn */
        box-shadow: 0 10px 25px rgba(255, 182, 193, 0.4);
        text-align: center; 
        border: 2px solid #ffccd5;
        max-width: 500px;
        margin: 20px auto;
        font-family: 'Quicksand', sans-serif;
    }

    .wish-text { color: #ff758f; font-size: 20px; line-height: 1.6; font-weight: 500; }
    .signature { font-family: 'Dancing Script', cursive; font-size: 32px; color: #ff4d6d; text-align: right; margin-top: 20px; }
    
    /* Nút bấm */
    .stButton { text-align: center; }
    .stButton>button {
        background: linear-gradient(45deg, #ff758f, #ffb3c1); color: white;
        border-radius: 25px; border: none; padding: 12px 40px; font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); }
    
    /* Xóa các khoảng trống thừa của Streamlit */
    .block-container { padding-top: 2rem; }
    </style>

    <div class="cherry-blossom" style="left:15%; animation-duration:7s;">🌸</div>
    <div class="cherry-blossom" style="left:45%; animation-duration:10s;">✨</div>
    <div class="cherry-blossom" style="left:85%; animation-duration:8s;">🌸</div>
    """, unsafe_allow_html=True)

# Link sticker con thỏ/mèo của bạn
capoo_sticker = "https://anhtomau.com/wp-content/uploads/2025/12/Sticker-cute-dong-dang-yeu.gif"

# --- LOGIC CHIA TRANG ---

if st.session_state.step == 'trang_keo_day':
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>🐰 Thỏ con chuyển phát quà... ✨</h2>", unsafe_allow_html=True)
    
    # Hiển thị sticker ở giữa
    st.image(capoo_sticker, width=280)
    
    st.write("")
    keo = st.select_slider("Kéo chú thỏ sang phải để nhận quà:", 
                           options=["🐰🌱", " 🐾🌿", "  🐾🍀", "   🐾🌷", "    🐰🌸"], 
                           key="slider_final")
    if "🌸" in keo:
        st.session_state.step = 'trang_mo_thu'
        st.rerun()

elif st.session_state.step == 'trang_mo_thu':
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>🎀 Bạn có một bức thư tay!</h2>", unsafe_allow_html=True)
    
    # Icon thư căn giữa, không còn khung trắng thừa
    st.image("https://cdn-icons-png.flaticon.com/512/4720/4720458.png", width=180)
    
    if st.button("Mở thư xem ngay ✨"):
        st.session_state.step = 'trang_noi_dung'
        st.rerun()

elif st.session_state.step == 'trang_noi_dung':
    st.balloons()
    
    # Phần nội dung nằm trong lá thiệp hình chữ nhật
    st.markdown(f"""
        <div class="the-thiep">
            <img src="{capoo_sticker}" width="150" style="margin-bottom: 20px;">
            <p class="wish-text">
                Chúc bạn một ngày thật rực rỡ và tràn đầy niềm vui!<br><br>
                Mong rằng nụ cười của bạn cũng sẽ đáng yêu và tinh nghịch như chú mèo Capoo này vậy. 🌸✨
            </p>
            <p class="signature">Ký tên: Huy ♡</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Đóng thư 🐾"):
        st.session_state.step = 'trang_keo_day'
        st.rerun()
