import streamlit as st

# 1. Cấu hình trang
st.set_page_config(page_title="Món quà từ Thỏ", page_icon="🌸", layout="centered")

# 2. Khởi tạo trạng thái
if 'step' not in st.session_state:
    st.session_state.step = 'keo_day'

# 3. CSS: Giao diện Cute + Hiệu ứng Hoa Anh Đào & Lá rơi
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&family=Zeyada&display=swap');

    .stApp {
        background-color: #fff0f3;
        overflow: hidden;
    }

    /* Hiệu ứng rơi */
    .falling {
        position: fixed;
        top: -10%;
        z-index: 9999;
        user-select: none;
        animation: fall linear infinite;
    }

    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
    }

    .f1 { left: 5%;  animation-duration: 7s; font-size: 20px; }
    .f2 { left: 20%; animation-duration: 10s; font-size: 25px; animation-delay: 2s; }
    .f3 { left: 40%; animation-duration: 8s; font-size: 18px; animation-delay: 4s; }
    .f4 { left: 60%; animation-duration: 12s; font-size: 22px; animation-delay: 1s; }
    .f5 { left: 80%; animation-duration: 9s; font-size: 24px; animation-delay: 3s; }
    .f6 { left: 90%; animation-duration: 11s; font-size: 20px; animation-delay: 5s; }

    /* Bức thư dập dềnh */
    .letter-paper {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 30px;
        border: 4px dotted #ffccd5;
        box-shadow: 0px 10px 25px rgba(255, 182, 193, 0.4);
        margin: 20px auto;
        max-width: 500px;
        animation: float 3s ease-in-out infinite;
        position: relative;
        z-index: 10;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }

    .letter-text { font-family: 'Quicksand', sans-serif; color: #ff758f; font-size: 18px; }
    .signature { font-family: 'Zeyada', cursive; font-size: 35px; color: #ff4d6d; text-align: right; }

    .stButton>button {
        background-color: #ffb3c1;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
    }
    </style>

    <div class="falling f1">🌸</div>
    <div class="falling f2">🍃</div>
    <div class="falling f3">🌸</div>
    <div class="falling f4">🍂</div>
    <div class="falling f5">🌸</div>
    <div class="falling f6">🍁</div>
    """, unsafe_allow_html=True)

# --- TRANG 1: KÉO DÂY ---
if st.session_state.step == 'keo_day':
    st.markdown("<h1 style='text-align: center; color: #ff758f;'>🐰 Thỏ con chuyển phát... ✨</h1>", unsafe_allow_html=True)
    # Đã đổi key thành rabbit_run_v2
    choice = st.select_slider("", options=["🐰🌱", " 🐾🌿", "  🐾🍀", "   🐾🌷", "    🐰🌸"], key="rabbit_run_v2")
    if "🌸" in choice:
        st.session_state.step = 'mo_thu'
        st.balloons()
        st.rerun()

# --- TRANG 2: PHONG THƯ ---
elif st.session_state.step == 'mo_thu':
    st.markdown("<div style='text-align: center; margin-top: 50px;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #ff758f;'>🎀 Có một bức thư cho bạn nè...</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4720/4720458.png", width=160) 
    # Đã đổi key thành open_btn_v2
    if st.button("Mở thư xem ngay ✨", key="open_btn_v2"):
        st.session_state.step = 'noi_dung'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- TRANG 3: NỘI DUNG ---
elif st.session_state.step == 'noi_dung':
    st.markdown("<h2 style='text-align: center; color: #ff758f;'>🌷 Lời nhắn từ trái tim 🌷</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="letter-paper">
            <div class="letter-text">
                <p>Chào bạn nè! ✨</p>
                <p>Thỏ con đã mang những cánh hoa và lá mùa thu đẹp nhất đến cho bạn đây.</p>
                <p>Hy vọng không gian này làm bạn cảm thấy thật ấm áp và hạnh phúc!</p>
            </div>
            <div class="signature">Ký tên: [Tên của bạn] ♡</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=1000", caption="Gửi ngàn cái ôm 🧸")

    # Đã đổi key thành back_btn_v2
    if st.button("Đóng thư lại 🐰", key="back_btn_v2"):
        st.session_state.step = 'keo_day'
        st.rerun()