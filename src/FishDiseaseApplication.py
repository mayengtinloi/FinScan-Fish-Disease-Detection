import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import time
from datetime import datetime
import base64

# --- Load model ---
@st.cache_resource
def get_model():
    return tf.keras.models.load_model('MobileNetV2.keras')

my_model = get_model()

labels_list = [
    "Bacterial Red Disease",
    "Aeromoniasis",
    "Healthy",
    "Parasitic Disease",
    "Viral White Tail Disease"
]

# --- Predict function ---
def check_fish(img):
    # Correct rotation using EXIF tag
    img = ImageOps.exif_transpose(img)

    # Convert to RGB and resize
    img = img.convert('RGB')
    img = img.resize((224, 224))

    # Convert to numpy array
    arr = np.array(img)

    # Remove alpha if present
    if arr.shape[-1] == 4:
        arr = arr[..., :3]

    # Normalize pixel values to [0, 1]
    arr = arr / 255.0

    # Add batch dimension
    arr = np.expand_dims(arr, axis=0)

    # Predict
    pred = my_model.predict(arr)

    # Get label and probability
    idx = np.argmax(pred)
    prob = float(np.max(pred))

    return labels_list[idx], prob, pred

# --- Translations ---
texts = {
    "en": {
        "welcome_title": "Welcome to IKAN.AI",
        "welcome_sub": "Smart Fish Disease Detection",
        "home_title": "Fish Disease Detection 🐟",
        "choose": "Choose option",
        "upload": "Upload image",
        "upload_file": "Upload a fish image",
        "camera": "Take a photo of your fish",
        "check": "Check Now",
        "checking": "Checking... 🩺",
        "result": "Result ✅",
        "status": "Status",
        "disease": "Disease",
        "confidence": "Confidence",
        "time": "Time",
        "guide": "Guide",
        "another": "Check Another",
        "guide_title": "Handling Guide 📝",
        "allow_camera": "Please allow camera permission first.",
        "your_image": "Your Image",
        "back_result": "Back to Result",
        "processing": "Processing...",
        "unable": "❌ Unable to detect. Try again.",
        "go_back": "Go Back"
    },
    "ms": {
        "welcome_title": "Selamat datang ke IKAN.AI",
        "welcome_sub": "Sistem Pintar Pengesanan Penyakit Ikan",
        "home_title": "Pengesanan Penyakit Ikan 🐟",
        "choose": "Pilih pilihan",
        "upload": "Muat naik imej",
        "upload_file": "Muat naik imej ikan",
        "camera": "Ambil gambar ikan anda",
        "check": "Periksa Sekarang",
        "checking": "Memeriksa... 🩺",
        "result": "Keputusan ✅",
        "status": "Status",
        "disease": "Penyakit",
        "confidence": "Keyakinan",
        "time": "Masa",
        "guide": "Panduan",
        "another": "Periksa Lagi",
        "guide_title": "Panduan Penjagaan 📝",
        "allow_camera": "Sila benarkan kebenaran kamera dahulu.",
        "your_image": "Imej Anda",
        "back_result": "Kembali ke Keputusan",
        "processing": "Sedang diproses...",
        "unable": "❌ Tidak dapat dikesan. Sila cuba lagi.",
        "go_back": "Kembali"
    },
    "zh": {
        "welcome_title": "欢迎来到 IKAN.AI",
        "welcome_sub": "智能鱼病检测系统",
        "home_title": "鱼病检测  🐟",
        "choose": "选择方式",
        "upload": "上传图片",
        "upload_file": "上传鱼的图片",
        "camera": "拍摄您的鱼",
        "check": "立即检查",
        "checking": "检查中... 🩺",
        "result": "结果 ✅",
        "status": "状态",
        "disease": "疾病",
        "confidence": "置信度",
        "time": "时间",
        "guide": "指南",
        "another": "再次检查",
        "guide_title": "处理指南 📝",
        "allow_camera": "请先允许相机权限。",
        "your_image": "您的图片",
        "back_result": "返回结果",
        "processing": "处理中...",
        "unable": "❌ 无法检测。请再试一次。",
        "go_back": "返回"
    }
}

# --- Style ---
def set_style(mode):
    bg = "#f2f9fb" if mode == "Light" else "#121212"
    text = "#222" if mode == "Light" else "#f0f0f0"
    card = "white" if mode == "Light" else "#1e1e1e"

    st.markdown(f"""
        <style>
            html, body {{
                background-color: {bg};
                color: {text};
            }}
            .block-container {{
                padding-top: 1rem !important;
                max-width: 420px;
                margin: auto;
                background: {card};
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            }}
            .stButton>button {{
                background-color: #0077b6;
                color: white;
                font-size: 18px;
                padding: 0.7em 1.5em;
                border-radius: 10px;
                border: none;
                width: 100%;
            }}
            .stRadio>div {{
                justify-content: center;
            }}
        </style>
    """, unsafe_allow_html=True)

# --- Welcome screen ---
def show_welcome(txt):
    logo_path = "logo.png"
    
    def img_to_b64(path_img):
        with open(path_img, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    logo_b64 = img_to_b64(logo_path)

    st.markdown(
        f"""
        <style>
            .welcome {{
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                background: linear-gradient(135deg, #00b4d8, #48cae4);
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                animation: fadeIn 2s;
                z-index: 9999;
            }}
            .welcome img {{
                max-width: 70%;
                height: auto;
                margin-bottom: 20px;
            }}
            .title {{
                font-size: 28px;
                font-weight: bold;
                color: white;
                margin-bottom: 10px;
                text-align: center;
            }}
            .subtitle {{
                font-size: 16px;
                color: white;
                text-align: center;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
        </style>
        <div class="welcome">
            <img src="data:image/png;base64,{logo_b64}" alt="Logo"/>
            <div class="title">{txt['welcome_title']}</div>
            <div class="subtitle">{txt['welcome_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(3)
    st.session_state.page_num = 0
    st.rerun()

# --- Home ---
def show_home(txt):
    st.title(txt["home_title"])
    option = st.radio(txt["choose"], [txt["upload"], txt["camera"]], horizontal=True)

    fish_img = None

    if option == txt["upload"]:
        st.markdown(f"**{txt['upload_file']} ({txt['your_image']})**")
        file = st.file_uploader("", type=["jpg", "jpeg", "png"])
        if file:
            fish_img = Image.open(file)
            st.image(fish_img, use_container_width=True, caption=txt["your_image"])
    else:
        st.warning(txt["allow_camera"])
        st.markdown(f"**{txt['camera']}**")
        cam_img = st.camera_input("")
        if cam_img:
            fish_img = Image.open(cam_img)
            # 👉 Do NOT show image preview here (remove st.image)

    if fish_img:
        st.session_state.img_data = fish_img
        if st.button(txt["check"]):
            st.session_state.page_num = 1
            st.rerun()


# --- Scan ---
def run_scan(txt):
    st.title(txt["checking"])
    prog = st.progress(0)
    msg = st.empty()
    for pct in range(101):
        time.sleep(0.015)
        prog.progress(pct)
        msg.text(f"{txt['processing']} {pct}%")

    label, prob, _ = check_fish(st.session_state.img_data)
    if prob < 0.6:
        st.error(txt["unable"])
        if st.button(txt["go_back"]):
            reset_all()
        return

    st.session_state.result_info = {
        "Condition": "Healthy" if label == "Healthy" else "Disease Detected",
        "Disease": label,
        "Confidence": f"{prob * 100:.1f}%",
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    st.session_state.page_num = 2
    st.rerun()

# --- Result ---
def show_output(txt):
    st.title(txt["result"])
    st.image(st.session_state.img_data, use_container_width=True)

    info = st.session_state.result_info
    st.markdown(f"""
    **{txt["status"]}:** {info['Condition']}  
    **{txt["disease"]}:** {info['Disease']}  
    **{txt["confidence"]}:** {info['Confidence']}  
    **{txt["time"]}:** {info['Time']}  
    """)

    if info["Disease"] != "Healthy":
        if st.button(txt["guide"]):
            st.session_state.page_num = 3
            st.rerun()

    if st.button(txt["another"]):
        reset_all()

# --- Guide ---
def show_guide(txt):
    st.title(txt["guide_title"])
    dis = st.session_state.result_info.get("Disease", "Healthy")
    lang = st.session_state.lang

    if dis == "Bacterial Red Disease":
        if lang == "English":
            st.markdown("""
            - Isolate infected fish immediately.
            - Use medicated feed with erythromycin for 7–10 days.
            - Improve water quality (increase aeration, reduce ammonia).
            - Reduce fish density to lower stress.
            - Regularly disinfect nets, tanks, and hands before handling fish.
            """)
        elif lang == "Malay":
            st.markdown("""
            - Asingkan ikan yang dijangkiti segera.
            - Gunakan makanan ubat dengan erythromycin selama 7–10 hari.
            - Baiki kualiti air (tambah pengudaraan, kurangkan ammonia).
            - Kurangkan kepadatan ikan untuk elak stres.
            - Sentiasa nyahkuman peralatan dan tangan sebelum pegang ikan.
            """)
        else:  # Chinese
            st.markdown("""
            - 立即隔离感染鱼只。
            - 使用含红霉素的药饲，连续 7–10 天。
            - 改善水质（增加充氧，减少氨含量）。
            - 降低密度以减少压力。
            - 定期消毒网具、池子及手部。
            """)

    elif dis == "Aeromoniasis":
        if lang == "English":
            st.markdown("""
            - Quarantine infected fish.
            - Administer oxytetracycline via feed or bath treatment for 5–7 days.
            - Clean pond bottoms and remove waste.
            - Improve water circulation and aeration.
            - Regularly monitor fish behavior and feeding.
            """)
        elif lang == "Malay":
            st.markdown("""
            - Kuarantin ikan yang dijangkiti.
            - Beri oxytetracycline melalui makanan atau rendaman selama 5–7 hari.
            - Bersihkan dasar kolam dan buang sisa.
            - Tambah peredaran air dan pengudaraan.
            - Pantau tingkah laku dan corak pemakanan ikan.
            """)
        else:  # Chinese
            st.markdown("""
            - 隔离感染鱼只。
            - 通过饲料或药浴给予土霉素，持续 5–7 天。
            - 清理池底，移除废物。
            - 改善水体循环及充氧。
            - 定期观察鱼只行为和摄食情况。
            """)

    elif dis == "Parasitic Disease":
        if lang == "English":
            st.markdown("""
            - Use salt (2–3%) or formalin baths for 30–60 minutes.
            - Avoid overcrowding.
            - Clean pond or tank regularly.
            - Use parasite control strategies (nets, screening).
            - Improve biosecurity to prevent future infections.
            """)
        elif lang == "Malay":
            st.markdown("""
            - Guna rendaman garam (2–3%) atau formalin selama 30–60 minit.
            - Elakkan kepadatan berlebihan.
            - Bersihkan kolam atau tangki secara berkala.
            - Guna langkah kawalan parasit (jaring, tapis).
            - Tingkatkan biosekuriti untuk mencegah jangkitan.
            """)
        else:  # Chinese
            st.markdown("""
            - 使用盐水（2–3%）或福尔马林药浴，持续 30–60 分钟。
            - 避免过度密集。
            - 定期清理池塘或水箱。
            - 采取寄生虫控制措施（网具、过滤）。
            - 加强生物安全，防止未来感染。
            """)

    elif dis == "Viral White Tail Disease":
        if lang == "English":
            st.markdown("""
            - No specific treatment available.
            - Immediately isolate infected fish to prevent spread.
            - Improve water quality and provide good nutrition.
            - Disinfect all equipment and facilities.
            - Remove severely affected fish if necessary.
            """)
        elif lang == "Malay":
            st.markdown("""
            - Tiada rawatan khusus.
            - Segera asingkan ikan yang dijangkiti untuk elak merebak.
            - Baiki kualiti air dan beri pemakanan baik.
            - Nyahkuman semua peralatan dan fasiliti.
            - Buang ikan yang teruk dijangkiti jika perlu.
            """)
        else:  # Chinese
            st.markdown("""
            - 无特效治疗。
            - 立即隔离感染鱼只以防扩散。
            - 改善水质，提供良好营养。
            - 消毒所有设备和设施。
            - 必要时淘汰严重感染鱼只。
            """)

    if st.button(txt["back_result"]):
        st.session_state.page_num = 2
        st.rerun()




# --- Reset ---
def reset_all():
    st.session_state.page_num = 0
    st.session_state.img_data = None
    st.session_state.result_info = None
    st.rerun()

# --- Main ---
def main():
    st.set_page_config(page_title="IKAN.AI", page_icon="🐟", layout="centered", initial_sidebar_state="collapsed")

    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "Light"
    if "lang" not in st.session_state:
        st.session_state.lang = "English"  # <-- use display name

    if "page_num" not in st.session_state:
        st.session_state.page_num = -1
    if "img_data" not in st.session_state:
        st.session_state.img_data = None

    lang_map = {"English": "en", "Malay": "ms", "中文": "zh"}
    lang_code = lang_map[st.session_state.lang]
    txt = texts[lang_code]

    set_style(st.session_state.theme_mode)

    if st.session_state.page_num == -1:
        show_welcome(txt)
    else:
        col1, col2 = st.columns(2)

        with col1:
            lang_selected = st.selectbox("🌐 Language", ["English", "Malay", "中文"], index=["English", "Malay", "中文"].index(st.session_state.lang))
            if lang_selected != st.session_state.lang:
                st.session_state.lang = lang_selected
                st.rerun()

        with col2:
            theme_selected = st.selectbox("🌗 Theme", ["Light", "Dark"], index=["Light", "Dark"].index(st.session_state.theme_mode))
            if theme_selected != st.session_state.theme_mode:
                st.session_state.theme_mode = theme_selected
                st.rerun()

    # Refresh translations again after possible update
    lang_code = lang_map[st.session_state.lang]
    txt = texts[lang_code]

    if st.session_state.page_num == 0:
        show_home(txt)
    elif st.session_state.page_num == 1:
        run_scan(txt)
    elif st.session_state.page_num == 2:
        show_output(txt)
    elif st.session_state.page_num == 3:
        show_guide(txt)




if __name__ == "__main__":
    main()
