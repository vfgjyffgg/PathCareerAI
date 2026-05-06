import streamlit as st

st.set_page_config(page_title="PathCareer AI", layout="wide")

st.markdown("""
<style>
header, #MainMenu, footer {visibility: hidden;}
.stApp { background: #F4F7FB; }
.block-container { padding: 35px 75px; }

h1,h2,h3,h4,h5,h6,p,label,span,div {
    color:#1F2937 !important;
}

/* CARD PUTIH */
.card {
    background:#FFFFFF;
    padding:34px;
    border-radius:26px;
    box-shadow:0 12px 30px rgba(15,23,42,0.08);
    margin-bottom:24px;
}

/* CARD BIRU GRADASI */
.blue-card, .result-blue {
    background: linear-gradient(135deg, #3F6F9F 0%, #6F98C4 55%, #9CC3EA 100%);
    padding:38px;
    border-radius:30px;
    box-shadow:0 16px 40px rgba(63,111,159,0.25);
    margin-bottom:26px;
}

/* PAKSA SEMUA TEKS DI BIRU JADI PUTIH */
.blue-card *,
.result-blue * {
    color:#FFFFFF !important;
}

.logo {
    font-size:32px;
    font-weight:900;
    letter-spacing:1px;
    color:#FFFFFF !important;
}

.hero {
    font-size:64px;
    font-weight:900;
    color:#FFFFFF !important;
    line-height:1;
    margin-top:26px;
}

.desc {
    color:#4B5563 !important;
    font-size:18px;
    line-height:1.6;
}

.desc-white {
    color:#F3F8FF !important;
    font-size:18px;
    line-height:1.6;
}

.info {
    background:#EAF2FF;
    padding:18px;
    border-radius:18px;
    border-left:6px solid #5B7FA6;
    margin-bottom:14px;
}

.result {
    background:#FFFFFF;
    padding:28px;
    border-radius:24px;
    border:1px solid #E5E7EB;
    box-shadow:0 8px 22px rgba(15,23,42,0.06);
    margin-bottom:18px;
}

.stButton button {
    background:#5B7FA6 !important;
    color:#FFFFFF !important;
    border:none !important;
    border-radius:999px !important;
    padding:12px 40px !important;
    font-weight:800 !important;
}

.stButton button * { color:#FFFFFF !important; }

.stTextInput input {
    background:#6F98C4 !important;
    color:#FFFFFF !important;
    border:none !important;
    border-radius:16px !important;
}

.stTextInput input::placeholder { color:#EAF2FF !important; }

div[data-baseweb="select"] > div {
    background:#6F98C4 !important;
    border:none !important;
    border-radius:16px !important;
}

div[data-baseweb="select"] * { color:#FFFFFF !important; }

ul[role="listbox"], li[role="option"] {
    background:#6F98C4 !important;
    color:#FFFFFF !important;
}

li[role="option"] * { color:#FFFFFF !important; }
li[role="option"]:hover { background:#5B7FA6 !important; }

span[data-baseweb="tag"] {
    background:#4A6C90 !important;
    color:#FFFFFF !important;
}

span[data-baseweb="tag"] * { color:#FFFFFF !important; }

.good {
    background:#DCFCE7;
    color:#166534 !important;
    padding:8px 14px;
    border-radius:999px;
    display:inline-block;
    margin:5px;
    font-weight:700;
}

.bad {
    background:#FEE2E2;
    color:#991B1B !important;
    padding:8px 14px;
    border-radius:999px;
    display:inline-block;
    margin:5px;
    font-weight:700;
}

.neutral {
    background:#EAF2FF;
    color:#315B84 !important;
    padding:8px 14px;
    border-radius:999px;
    display:inline-block;
    margin:5px;
    font-weight:700;
}

.percent {
    color:#5B7FA6 !important;
    font-weight:900;
    font-size:24px;
}

.metric-box {
    background:#FFFFFF;
    padding:20px;
    border-radius:20px;
    border:1px solid #E5E7EB;
    text-align:center;
    box-shadow:0 8px 20px rgba(15,23,42,0.05);
}

.metric-box h2 { color:#5B7FA6 !important; }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

hard_skills = ["Coding", "Data Analysis", "Design", "Video Editing", "Microsoft Excel", "Digital Marketing"]
soft_skills = ["Public Speaking", "Communication", "Leadership", "Problem Solving", "Teamwork"]
competition_options = ["Lomba Desain", "Lomba Coding", "Lomba Bisnis", "Lomba Karya Tulis", "Lomba Konten", "Belum Pernah"]
education_options = ["Pilih pendidikan terakhirmu", "SMA/SMK", "D3", "S1", "S2"]

jobs = [
    {
        "title": "Data Analyst Intern",
        "required_hard": ["Data Analysis", "Microsoft Excel", "Coding"],
        "required_soft": ["Problem Solving", "Communication"],
        "education": ["D3", "S1"],
        "preferred_competition": ["Lomba Karya Tulis", "Lomba Bisnis"],
        "desc": "Cocok untuk mahasiswa yang suka membaca data, membuat laporan, dan menemukan insight dari angka."
    },
    {
        "title": "UI/UX Designer Intern",
        "required_hard": ["Design"],
        "required_soft": ["Communication", "Problem Solving"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Desain", "Lomba Konten"],
        "desc": "Cocok untuk mahasiswa yang suka desain tampilan aplikasi, user flow, dan pengalaman pengguna."
    },
    {
        "title": "Content Creator Intern",
        "required_hard": ["Video Editing", "Design"],
        "required_soft": ["Public Speaking", "Communication"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Konten", "Lomba Desain"],
        "desc": "Cocok untuk mahasiswa yang suka membuat video, konten media sosial, dan komunikasi visual."
    },
    {
        "title": "Web Developer Intern",
        "required_hard": ["Coding"],
        "required_soft": ["Problem Solving", "Teamwork"],
        "education": ["D3", "S1"],
        "preferred_competition": ["Lomba Coding"],
        "desc": "Cocok untuk mahasiswa yang suka membuat website, menyusun logika, dan membangun sistem."
    },
    {
        "title": "Digital Marketing Intern",
        "required_hard": ["Digital Marketing", "Microsoft Excel", "Design"],
        "required_soft": ["Communication", "Public Speaking"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Bisnis", "Lomba Konten"],
        "desc": "Cocok untuk mahasiswa yang tertarik promosi digital, campaign, konten, dan analisis performa."
    }
]

learning_tips = {
    "Coding": "Pelajari dasar pemrograman seperti variabel, kondisi, perulangan, dan function. Setelah itu buat project sederhana seperti website profil atau kalkulator.",
    "Data Analysis": "Latihan membaca data, membuat grafik, menghitung rata-rata/persentase, dan membuat kesimpulan dari data.",
    "Design": "Latihan membuat poster, UI sederhana, layout landing page, dan belajar komposisi warna serta typography.",
    "Video Editing": "Pelajari cut video, subtitle, transisi, audio, color adjustment, dan thumbnail untuk video pendek.",
    "Microsoft Excel": "Pelajari rumus IF, VLOOKUP/XLOOKUP, Pivot Table, grafik, dan dashboard sederhana.",
    "Digital Marketing": "Pelajari content planning, copywriting, social media strategy, dan basic ads.",
    "Public Speaking": "Latihan presentasi 1-2 menit, rekam diri sendiri, lalu evaluasi artikulasi, ekspresi, dan kejelasan pesan.",
    "Communication": "Latihan menjelaskan ide secara singkat, jelas, dan terstruktur.",
    "Leadership": "Ikut project kelompok atau organisasi kecil untuk melatih koordinasi, pembagian tugas, dan pengambilan keputusan.",
    "Problem Solving": "Latihan membedah masalah dengan pola: masalah utama, penyebab, alternatif solusi, dan langkah pengerjaan.",
    "Teamwork": "Biasakan bekerja dalam tim, memberi update progress, menerima feedback, dan menyelesaikan konflik kecil."
}

def score_job(education, competitions, selected_hard, selected_soft, job):
    hard_match = [s for s in job["required_hard"] if s in selected_hard]
    soft_match = [s for s in job["required_soft"] if s in selected_soft]
    hard_score = (len(hard_match) / len(job["required_hard"])) * 45
    soft_score = (len(soft_match) / len(job["required_soft"])) * 30
    edu_score = 15 if education in job["education"] else 0
    competition_match = [c for c in competitions if c in job["preferred_competition"]]
    comp_score = 10 if competition_match else 0
    score = int(hard_score + soft_score + edu_score + comp_score)
    missing_hard = [s for s in job["required_hard"] if s not in selected_hard]
    missing_soft = [s for s in job["required_soft"] if s not in selected_soft]
    return score, hard_match, soft_match, missing_hard, missing_soft

def readiness_level(score):
    if score >= 80:
        return "Sangat Siap", "Profil kamu sudah sangat sesuai dengan pekerjaan ini."
    elif score >= 60:
        return "Cukup Siap", "Profil kamu sudah cukup sesuai, tetapi masih ada beberapa skill yang perlu ditingkatkan."
    elif score >= 40:
        return "Perlu Pengembangan", "Kamu memiliki dasar yang relevan, tetapi masih perlu memperkuat beberapa skill utama."
    else:
        return "Belum Siap", "Profil kamu masih perlu banyak dikembangkan untuk posisi ini."

def analyze_profile():
    results = []
    for job in jobs:
        score, hard_match, soft_match, missing_hard, missing_soft = score_job(
            st.session_state.education,
            st.session_state.competitions,
            st.session_state.selected_hard,
            st.session_state.selected_soft,
            job
        )
        results.append({
            **job,
            "score": score,
            "hard_match": hard_match,
            "soft_match": soft_match,
            "missing_hard": missing_hard,
            "missing_soft": missing_soft
        })
    return sorted(results, key=lambda x: x["score"], reverse=True)

if st.session_state.page == "home":
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="blue-card">
            <div class="logo">PATHCAREER AI</div>
            <p class="desc-white">
            Sistem rekomendasi pekerjaan berbasis profil mahasiswa.
            Analisis pendidikan, lomba/prestasi, hard skill, dan soft skill untuk menemukan
            career path yang paling sesuai.
            </p>
            <div class="hero">Build Your<br>Career Path<br>Smarter</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("MULAI"):
            st.session_state.page = "form"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="card">
            <h3>Fitur Sistem</h3>
            <div class="info"><b>🎓 Analisis Pendidikan</b><br>Menyesuaikan lowongan dengan jenjang pendidikan pengguna.</div>
            <div class="info"><b>🏆 Analisis Lomba</b><br>Menghitung pengalaman lomba/prestasi yang relevan.</div>
            <div class="info"><b>🧠 Skill Matching</b><br>Mencocokkan hard skill dan soft skill dengan kebutuhan pekerjaan.</div>
            <div class="info"><b>📚 Roadmap Belajar</b><br>Memberi saran pengembangan berdasarkan skill gap.</div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "form":
    if st.button("← Kembali"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <div class="card">
        <h1>Isi Profil Pengguna</h1>
        <p class="desc">Isi data berikut agar sistem dapat menganalisis kecocokan kamu dengan beberapa pilihan pekerjaan.</p>
    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input("Nama pengguna", placeholder="Masukkan nama kamu")
    education = st.selectbox("Pendidikan terakhir", education_options)
    competitions = st.multiselect("Lomba / prestasi yang pernah diikuti", competition_options, placeholder="Pilih satu atau lebih")
    selected_hard = st.multiselect("Hard skill yang kamu miliki", hard_skills, placeholder="Choose your hard skill")
    selected_soft = st.multiselect("Soft skill yang kamu miliki", soft_skills, placeholder="Choose your soft skill")

    if st.button("Lihat Hasil Analisis"):
        if not nama.strip():
            st.warning("Masukkan nama dulu.")
            st.stop()

        if education == "Pilih pendidikan terakhirmu":
            st.warning("Pilih pendidikan terakhir dulu.")
            st.stop()

        if not selected_hard and not selected_soft:
            st.warning("Pilih minimal satu hard skill atau soft skill.")
            st.stop()

        st.session_state.nama = nama
        st.session_state.education = education
        st.session_state.competitions = competitions
        st.session_state.selected_hard = selected_hard
        st.session_state.selected_soft = selected_soft
        st.session_state.page = "result"
        st.rerun()

elif st.session_state.page == "result":
    if st.button("← Edit Profil"):
        st.session_state.page = "form"
        st.rerun()

    results = analyze_profile()
    best = results[0]
    level, level_desc = readiness_level(best["score"])

    st.markdown(f"""
    <div class="result-blue">
        <h2>Hasil Analisis untuk {st.session_state.nama}</h2>
        <h1>{best['title']}</h1>
        <p>{best['desc']}</p>
        <h3>Kecocokan: {best['score']}%</h3>
        <p><b>Career Readiness:</b> {level}</p>
        <p>{level_desc}</p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(best["score"] / 100)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-box">
            <h2>{st.session_state.education}</h2>
            <p>Pendidikan</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-box">
            <h2>{len(st.session_state.competitions)}</h2>
            <p>Lomba/Prestasi</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        total_skill = len(st.session_state.selected_hard) + len(st.session_state.selected_soft)
        st.markdown(f"""
        <div class="metric-box">
            <h2>{total_skill}</h2>
            <p>Total Skill</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Ringkasan Profil")
    ringkasan_html = '<div class="result">'
    ringkasan_html += "<h4>Hard Skill</h4>"
    for s in st.session_state.selected_hard:
        ringkasan_html += f'<span class="neutral">{s}</span>'
    ringkasan_html += "<h4>Soft Skill</h4>"
    for s in st.session_state.selected_soft:
        ringkasan_html += f'<span class="neutral">{s}</span>'
    ringkasan_html += "<h4>Lomba / Prestasi</h4>"
    if st.session_state.competitions:
        for c in st.session_state.competitions:
            ringkasan_html += f'<span class="neutral">{c}</span>'
    else:
        ringkasan_html += "<p>Belum ada lomba/prestasi yang dipilih.</p>"
    ringkasan_html += "</div>"
    st.markdown(ringkasan_html, unsafe_allow_html=True)

    st.subheader("Skill yang Sudah Cocok")
    matched_all = best["hard_match"] + best["soft_match"]
    for s in matched_all:
        st.markdown(f'<span class="good">{s}</span>', unsafe_allow_html=True)

    st.subheader("Skill Gap")
    missing_all = best["missing_hard"] + best["missing_soft"]
    if missing_all:
        for s in missing_all:
            st.markdown(f'<span class="bad">{s}</span>', unsafe_allow_html=True)
    else:
        st.success("Skill utama sudah sesuai.")

    st.subheader("Saran Pengembangan")
    if missing_all:
        for s in missing_all:
            st.markdown(f"""
            <div class="info">
                <b>{s}</b><br>
                {learning_tips.get(s, "Pelajari dasar skill ini lalu buat project sederhana.")}
            </div>
            """, unsafe_allow_html=True)

    st.subheader("Ranking Semua Pekerjaan")
    for item in results:
        item_level, _ = readiness_level(item["score"])
        st.markdown(f"""
        <div class="result">
            <h3>{item['title']}</h3>
            <p>{item['desc']}</p>
            <div class="percent">Kecocokan: {item['score']}%</div>
            <p><b>Status:</b> {item_level}</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(item["score"] / 100)
