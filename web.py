import streamlit as st

# 1. Cấu hình trang
st.set_page_config(page_title="Quà tặng đặc biệt", page_icon="🐱", layout="centered")

# 2. Khởi tạo trạng thái (Để chia màn hình rõ ràng)
if 'step' not in st.session_state:
    st.session_state.step = 'trang_keo_day'

# 3. Giao diện CSS (Hoa rơi lấp lánh)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&family=Dancing+Script:wght@700&display=swap');
    .stApp { background-color: #fff0f3; overflow: hidden; }
    .cherry-blossom { position: fixed; top: -10%; z-index: 9999; user-select: none; animation: fall linear infinite; }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); opacity: 1; } 100% { transform: translateY(110vh) rotate(360deg); opacity: 0; } }
    .main-card {
        background: white; padding: 30px; border-radius: 30px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.5);
        text-align: center; border: 2px solid #ffccd5;
    }
    .wish-text { font-family: 'Quicksand', sans-serif; color: #ff758f; font-size: 20px; line-height: 1.6; }
    .signature { font-family: 'Dancing Script', cursive; font-size: 35px; color: #ff4d6d; text-align: right; }
    .stButton>button {
        background: linear-gradient(45deg, #ff758f, #ffb3c1); color: white;
        border-radius: 25px; border: none; padding: 12px 40px; font-weight: bold;
    }
    </style>
    <div class="cherry-blossom" style="left:15%; animation-duration:7s;">🌸</div>
    <div class="cherry-blossom" style="left:55%; animation-duration:10s;">✨</div>
    <div class="cherry-blossom" style="left:85%; animation-duration:8s;">🌸</div>
    """, unsafe_allow_html=True)

# Link sticker của bạn
capoo_sticker = "https://anhtomau.com/wp-content/uploads/2025/12/Sticker-cute-dong-dang-yeu.gif"

# --- LOGIC ĐIỀU HƯỚNG CHỈ 1 LUỒNG DUY NHẤT ---

if st.session_state.step == 'trang_keo_day':
    # MÀN HÌNH 1: CHỈ CÓ 1 THANH KÉO
    st.markdown("<h2 style='text-align: center; color: #ff758f;'>🐰 Thỏ con chuyển phát quà... ✨</h2>", unsafe_allow_html=True)
    st.image(capoo_sticker, width=250)
    keo = st.select_slider("Kéo chú thỏ sang phải để nhận quà:", 
                           options=["🐰🌱", " 🐾🌿", "  🐾🍀", "   🐾🌷", "    🐰🌸"], 
                           key="slider_unique_final")
    if "🌸" in keo:
        st.session_state.step = 'trang_mo_thu'
        st.rerun()

elif st.session_state.step == 'trang_mo_thu':
    # MÀN HÌNH 2: CHỈ CÓ 1 NÚT BẤM
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4720/4720458.png", width=150)
    st.markdown("<h2 style='color: #ff758f;'>🎀 Bạn có một bức thư tay!</h2>", unsafe_allow_html=True)
    if st.button("Mở thư xem ngay ✨"):
        st.session_state.step = 'trang_noi_dung'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.step == 'trang_noi_dung':
    # MÀN HÌNH 3: NỘI DUNG THƯ
    st.balloons()
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.image(capoo_sticker, width=150)
    st.markdown(f"""
        <div style="text-align: left;">
            <p class="wish-text">
                Chúc bạn một ngày thật rực rỡ và tràn đầy niềm vui!<br><br>
                Mong rằng nụ cười của bạn cũng sẽ đáng yêu như chú mèo Capoo này vậy. 🌸✨
            </p>
            <p class="signature">Ký tên: [Tên của bạn] ♡</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Đóng thư 🐾"):
        st.session_state.step = 'trang_keo_day'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
