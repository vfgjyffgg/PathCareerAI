import streamlit as st

st.set_page_config(page_title="PathCareer AI", layout="wide")

st.markdown("""
<style>
header[data-testid="stHeader"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.stApp {
    background: #F8FAFC;
}

.block-container {
    padding-top: 40px;
    padding-left: 70px;
    padding-right: 70px;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #111827 !important;
}

.card {
    background: #FFFFFF;
    padding: 38px;
    border-radius: 28px;
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
    margin-bottom: 28px;
}

.brand {
    font-size: 30px;
    font-weight: 900;
    color: #111827 !important;
}

.desc {
    font-size: 21px;
    line-height: 1.5;
    color: #374151 !important;
    margin-top: 12px;
}

.hero-title {
    font-size: 76px;
    font-weight: 900;
    color: #4F7FAE !important;
    line-height: 0.95;
    margin-top: 30px;
}

.feature-card {
    background: #EEF5FF;
    padding: 24px;
    border-radius: 22px;
    border-left: 7px solid #4F7FAE;
    margin-bottom: 18px;
}

.feature-card b {
    color: #111827 !important;
    font-size: 18px;
}

.feature-card p {
    color: #4B5563 !important;
    font-size: 15px;
}

.stButton button {
    background-color: #4F7FAE !important;
    color: #FFFFFF !important;
    border-radius: 999px !important;
    border: none !important;
    padding: 13px 42px !important;
    font-size: 17px !important;
    font-weight: 800 !important;
}

.stButton button * {
    color: #FFFFFF !important;
}

.stButton button:hover {
    background-color: #3E6B96 !important;
}

/* INPUT NAMA */
.stTextInput input {
    background-color: #5F89B8 !important;
    color: #FFFFFF !important;
    border: 2px solid #4F7FAE !important;
    border-radius: 16px !important;
    font-size: 17px !important;
}

.stTextInput input::placeholder {
    color: #EAF2FF !important;
}

/* SELECT SKILL */
div[data-baseweb="select"] {
    background-color: #5F89B8 !important;
    border-radius: 16px !important;
}

div[data-baseweb="select"] div,
div[data-baseweb="select"] span {
    color: #FFFFFF !important;
}

div[data-baseweb="select"] input {
    color: #FFFFFF !important;
}

div[data-baseweb="popover"] {
    background-color: #5F89B8 !important;
}

ul[role="listbox"] {
    background-color: #5F89B8 !important;
    border-radius: 16px !important;
}

li[role="option"] {
    background-color: #5F89B8 !important;
    color: #FFFFFF !important;
}

li[role="option"] div,
li[role="option"] span {
    color: #FFFFFF !important;
}

li[role="option"]:hover {
    background-color: #4F7FAE !important;
}

/* TAG SKILL */
span[data-baseweb="tag"] {
    background-color: #3E6B96 !important;
    color: #FFFFFF !important;
}

span[data-baseweb="tag"] span {
    color: #FFFFFF !important;
}

.result-card {
    background: #FFFFFF;
    padding: 30px;
    border-radius: 24px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.06);
    margin-top: 20px;
    margin-bottom: 20px;
}

.skill-good {
    background: #DCFCE7;
    color: #166534 !important;
    padding: 8px 14px;
    border-radius: 999px;
    display: inline-block;
    margin: 5px;
    font-weight: 700;
}

.skill-missing {
    background: #FEE2E2;
    color: #991B1B !important;
    padding: 8px 14px;
    border-radius: 999px;
    display: inline-block;
    margin: 5px;
    font-weight: 700;
}

.percent-box {
    background: #EEF5FF;
    padding: 14px 18px;
    border-radius: 16px;
    display: inline-block;
    font-weight: 800;
    color: #4F7FAE !important;
}

.small-muted {
    color: #6B7280 !important;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

careers = {
    "Content Creator": {
        "skills": ["Public Speaking", "Editing", "Gambar"],
        "desc": "Cocok untuk kamu yang suka membuat konten, berbicara di depan kamera, mengedit, dan membuat visual menarik.",
        "tips": {
            "Public Speaking": "Latihan berbicara 1-2 menit di depan kamera, lalu evaluasi suara, ekspresi, dan kejelasan penyampaian.",
            "Editing": "Pelajari dasar edit video seperti cut, transisi, subtitle, audio, dan color adjustment.",
            "Gambar": "Latihan membuat thumbnail, poster, atau layout visual sederhana agar konten terlihat lebih menarik."
        }
    },
    "Programmer / Web Developer": {
        "skills": ["Coding", "Menghitung"],
        "desc": "Cocok untuk kamu yang suka membuat program, menyusun logika, dan membangun website atau aplikasi sederhana.",
        "tips": {
            "Coding": "Pelajari dasar pemrograman seperti variabel, kondisi, perulangan, function, lalu buat project kecil.",
            "Menghitung": "Latihan logika matematika dasar, algoritma sederhana, dan pemecahan masalah secara sistematis."
        }
    },
    "Data Analyst": {
        "skills": ["Menghitung", "Coding"],
        "desc": "Cocok untuk kamu yang suka membaca data, menghitung, membuat laporan, dan mencari pola dari angka.",
        "tips": {
            "Menghitung": "Pelajari statistik dasar seperti rata-rata, persentase, perbandingan, dan cara membaca grafik.",
            "Coding": "Pelajari Python atau spreadsheet untuk mengolah data sederhana dan membuat visualisasi."
        }
    },
    "UI/UX Designer": {
        "skills": ["Gambar", "Editing"],
        "desc": "Cocok untuk kamu yang suka desain tampilan aplikasi, membuat layout, dan menyusun pengalaman pengguna.",
        "tips": {
            "Gambar": "Latihan membuat wireframe, layout aplikasi, dan komposisi warna yang rapi.",
            "Editing": "Pelajari cara merapikan visual, memilih font, mengatur spacing, dan membuat prototype sederhana."
        }
    },
    "Digital Marketer": {
        "skills": ["Public Speaking", "Editing"],
        "desc": "Cocok untuk kamu yang tertarik promosi digital, membuat konten, dan menyampaikan pesan produk ke audiens.",
        "tips": {
            "Public Speaking": "Latihan membuat script promosi singkat yang jelas, persuasif, dan mudah dipahami.",
            "Editing": "Pelajari desain konten promosi, video pendek, dan visual iklan sederhana."
        }
    }
}

skill_options = ["Public Speaking", "Coding", "Editing", "Menghitung", "Gambar"]

if st.session_state.page == "home":
    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("""
        <div class="card">
            <div class="brand">PATHCAREER AI</div>
            <p class="desc">
            PathCareer adalah sistem AI yang membantu mahasiswa menemukan karier yang sesuai
            berdasarkan skill yang dimiliki, lalu memberikan rekomendasi pembelajaran untuk
            meningkatkan kemampuan.
            </p>
            <div class="hero-title">
            Find Your<br>
            Path, Build<br>
            Your Future
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("MULAI"):
            st.session_state.page = "analysis"
            st.rerun()

    with right:
        st.markdown("""
        <div class="card">
            <h3>Kenapa PathCareer?</h3>
            <div class="feature-card">
                <b>🎯 Rekomendasi Karier</b>
                <p>Sistem mencocokkan skill kamu dengan pilihan karier yang relevan.</p>
            </div>
            <div class="feature-card">
                <b>📊 Skill Gap Analysis</b>
                <p>Sistem menunjukkan skill yang sudah cocok dan skill yang masih perlu dipelajari.</p>
            </div>
            <div class="feature-card">
                <b>📚 Roadmap Belajar</b>
                <p>Kamu mendapat saran belajar yang sesuai dengan skill yang belum dikuasai.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    if st.button("← Kembali"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <div class="card">
        <h1>Analisis Karier Mahasiswa</h1>
        <p class="small-muted">
        Pilih skill yang kamu miliki. Sistem akan menghitung kecocokan karier,
        menampilkan skill gap, dan memberikan tips belajar yang lebih spesifik.
        </p>
    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input("Nama kamu", placeholder="Masukkan nama kamu")

    selected_skills = st.multiselect(
        "Pilih skill yang kamu miliki",
        skill_options,
        placeholder="Choose your option"
    )

    if st.button("Analisis Sekarang"):
        if not selected_skills:
            st.warning("Pilih minimal satu skill dulu.")
            st.stop()

        hasil = []

        for career_name, data in careers.items():
            required = data["skills"]
            cocok = [skill for skill in required if skill in selected_skills]
            kurang = [skill for skill in required if skill not in selected_skills]
            score = int((len(cocok) / len(required)) * 100)

            hasil.append({
                "career": career_name,
                "score": score,
                "desc": data["desc"],
                "cocok": cocok,
                "kurang": kurang,
                "tips": data["tips"]
            })

        hasil = sorted(hasil, key=lambda x: x["score"], reverse=True)
        terbaik = hasil[0]

        st.markdown(f"""
        <div class="result-card">
            <h2>Rekomendasi Karier Terbaik</h2>
            <h1 style="color:#4F7FAE !important;">{terbaik['career']}</h1>
            <p>{terbaik['desc']}</p>
            <div class="percent-box">Tingkat Kecocokan: {terbaik['score']}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(terbaik["score"] / 100)

        st.markdown("<h3>Skill yang Sudah Sesuai</h3>", unsafe_allow_html=True)
        if terbaik["cocok"]:
            html = ""
            for skill in terbaik["cocok"]:
                html += f'<span class="skill-good">{skill}</span>'
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write("Belum ada skill yang cocok dengan karier ini.")

        st.markdown("<h3>Skill Gap / Skill yang Perlu Dipelajari</h3>", unsafe_allow_html=True)
        if terbaik["kurang"]:
            html = ""
            for skill in terbaik["kurang"]:
                html += f'<span class="skill-missing">{skill}</span>'
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.success("Semua skill utama sudah sesuai.")

        st.markdown("<h3>Roadmap Belajar yang Disarankan</h3>", unsafe_allow_html=True)

        if terbaik["kurang"]:
            for i, skill in enumerate(terbaik["kurang"], start=1):
                tip = terbaik["tips"][skill]
                st.markdown(f"""
                <div class="feature-card">
                    <h4>{i}. Pelajari {skill}</h4>
                    <p>{tip}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="feature-card">
                <h4>Lanjut ke Portofolio</h4>
                <p>Kamu bisa mulai membuat project kecil, sertifikasi, atau portofolio sesuai bidang karier yang direkomendasikan.</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<h3>Ranking Semua Karier</h3>", unsafe_allow_html=True)

        for item in hasil:
            st.markdown(f"""
            <div class="result-card">
                <h4>{item['career']}</h4>
                <p>{item['desc']}</p>
                <div class="percent-box">Kecocokan: {item['score']}%</div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(item["score"] / 100)
