import streamlit as st

st.set_page_config(page_title="PathCareer AI", layout="wide")

st.markdown("""
<style>
header, #MainMenu, footer {visibility: hidden;}
.stApp { background: #F4F7FB; }
.block-container { padding: 35px 75px; max-width: 100%; }

h1,h2,h3,h4,h5,h6,p,label,span,div {
    color:#1F2937 !important;
}

.card {
    background:#FFFFFF;
    padding:34px;
    border-radius:26px;
    box-shadow:0 12px 30px rgba(15,23,42,0.08);
    margin-bottom:24px;
}

.blue-card, .result-blue {
    background: linear-gradient(135deg, #3F6F9F 0%, #6F98C4 55%, #9CC3EA 100%);
    padding:38px;
    border-radius:30px;
    box-shadow:0 16px 40px rgba(63,111,159,0.25);
    margin-bottom:26px;
}

.blue-card *, .result-blue * {
    color:#FFFFFF !important;
}

.logo {
    font-size:32px;
    font-weight:900;
    letter-spacing:1px;
}

.hero {
    font-size:64px;
    font-weight:900;
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

.stTextInput input::placeholder {
    color:#EAF2FF !important;
}

div[data-baseweb="select"] > div {
    background:#6F98C4 !important;
    border:none !important;
    border-radius:16px !important;
}

div[data-baseweb="select"] * {
    color:#FFFFFF !important;
}

ul[role="listbox"], li[role="option"] {
    background:#6F98C4 !important;
    color:#FFFFFF !important;
}

li[role="option"] * {
    color:#FFFFFF !important;
}

li[role="option"]:hover {
    background:#5B7FA6 !important;
}

span[data-baseweb="tag"] {
    background:#4A6C90 !important;
    color:#FFFFFF !important;
}

span[data-baseweb="tag"] * {
    color:#FFFFFF !important;
}

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

.metric-box h2 {
    color:#5B7FA6 !important;
}

.glints-btn {
    display:inline-block;
    background:#5B7FA6;
    color:#FFFFFF !important;
    border:none;
    border-radius:999px;
    padding:12px 32px;
    font-weight:800;
    text-decoration:none;
    margin-top:12px;
}

.glints-btn:hover {
    background:#4A6C90;
    color:#FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

hard_skills = [
    "Coding",
    "Data Analisis",
    "Design",
    "Video Editing",
    "Microsoft Excel",
    "Digital Marketing",
    "UI/UX Design",
    "Content Writing"
]

soft_skills = [
    "Public Speaking",
    "Leadership",
    "Problem Solving",
    "Teamwork",
    "Kreatif"
]

competition_options = [
    "Lomba Desain",
    "Lomba Coding",
    "Lomba Bisnis",
    "Lomba Karya Tulis",
    "Lomba Konten",
    "Belum Pernah"
]

education_options = [
    "Pilih pendidikan terakhirmu",
    "SMA/SMK",
    "D3",
    "S1",
    "S2"
]

jobs = [
    {
        "title": "Data Analyst",
        "required_hard": ["Data Analisis", "Microsoft Excel", "Coding"],
        "required_soft": ["Problem Solving", "Leadership"],
        "education": ["D3", "S1", "S2"],
        "preferred_competition": ["Lomba Karya Tulis", "Lomba Bisnis"],
        "desc": "Cocok untuk pengguna yang suka menganalisis data, membaca pola, membuat laporan, dan menemukan insight dari angka untuk membantu pengambilan keputusan.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=data+analyst&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    },
    {
        "title": "UI/UX Designer",
        "required_hard": ["UI/UX Design", "Design"],
        "required_soft": ["Kreatif", "Problem Solving"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Desain", "Lomba Konten"],
        "desc": "Cocok untuk pengguna yang tertarik membuat tampilan aplikasi atau website yang menarik, nyaman digunakan, dan mudah dipahami pengguna.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=ui%2Fux+design&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    },
    {
        "title": "Content Creator",
        "required_hard": ["Video Editing", "Design"],
        "required_soft": ["Public Speaking", "Kreatif"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Konten", "Lomba Desain"],
        "desc": "Cocok untuk pengguna yang suka membuat video, konten media sosial, dan menyampaikan ide kreatif melalui visual maupun audio.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=content+creator&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    },
    {
        "title": "Web Developer",
        "required_hard": ["Coding"],
        "required_soft": ["Problem Solving", "Teamwork"],
        "education": ["D3", "S1", "S2"],
        "preferred_competition": ["Lomba Coding"],
        "desc": "Cocok untuk pengguna yang suka membuat website, membangun sistem, dan menyusun logika pemrograman.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=web+developer&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    },
    {
        "title": "Digital Marketing Specialist",
        "required_hard": ["Digital Marketing", "Microsoft Excel", "Design"],
        "required_soft": ["Public Speaking", "Kreatif"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Bisnis", "Lomba Konten"],
        "desc": "Cocok untuk pengguna yang tertarik dalam strategi promosi digital, campaign media sosial, dan analisis performa pemasaran.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=digital+marketing+specialist&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    },
    {
        "title": "Social Media Specialist",
        "required_hard": ["Digital Marketing", "Design", "Video Editing"],
        "required_soft": ["Public Speaking", "Kreatif"],
        "education": ["SMA/SMK", "D3", "S1"],
        "preferred_competition": ["Lomba Konten", "Lomba Bisnis"],
        "desc": "Cocok untuk pengguna yang suka mengelola media sosial, membuat strategi konten, dan meningkatkan engagement audience.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=MEDIA+SOCIAL+SPECIALIST&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    },
    {
        "title": "Content Writer",
        "required_hard": ["Content Writing"],
        "required_soft": ["Kreatif", "Leadership"],
        "education": ["SMA/SMK", "D3", "S1", "S2"],
        "preferred_competition": ["Lomba Karya Tulis", "Lomba Konten"],
        "desc": "Cocok untuk pengguna yang suka menulis artikel, karya ilmiah, blog, dan membuat konten berbasis tulisan.",
        "glints_link": "https://glints.com/id/opportunities/jobs/explore?keyword=CONTENT+WRITER&country=ID&locationName=All+Cities%2FProvinces&lowestLocationLevel=1"
    }
]

learning_tips = {
    "Coding": "Pelajari HTML, CSS, JavaScript, serta dasar Python atau SQL. Setelah itu buat project sederhana seperti website profil, kalkulator, atau dashboard kecil.",
    "Data Analisis": "Pelajari cara membaca data, membuat grafik, dashboard sederhana, serta memahami pola dan insight dari data.",
    "Design": "Latihan membuat poster, thumbnail, layout media sosial, dan pahami komposisi warna, typography, serta visual hierarchy.",
    "Video Editing": "Pelajari cut video, subtitle, transisi, audio, color grading, dan pembuatan video pendek untuk media sosial.",
    "Microsoft Excel": "Pelajari rumus IF, VLOOKUP/XLOOKUP, Pivot Table, grafik, dan dashboard sederhana.",
    "Digital Marketing": "Pelajari social media strategy, copywriting, SEO dasar, content planning, dan analisis performa campaign.",
    "UI/UX Design": "Pelajari wireframe, user flow, prototype, usability, dan desain interface menggunakan Figma.",
    "Content Writing": "Latihan menulis artikel, blog, caption, dan karya ilmiah secara terstruktur dengan bahasa yang jelas.",
    "Public Speaking": "Latihan presentasi singkat, rekam diri sendiri, lalu evaluasi artikulasi, ekspresi, dan kejelasan pesan.",
    "Leadership": "Ikut project kelompok atau organisasi kecil untuk melatih koordinasi, pembagian tugas, dan pengambilan keputusan.",
    "Problem Solving": "Latihan membedah masalah dengan pola: masalah utama, penyebab, alternatif solusi, dan langkah pengerjaan.",
    "Teamwork": "Biasakan bekerja dalam tim, memberi update progress, menerima feedback, dan menyelesaikan konflik kecil.",
    "Kreatif": "Biasakan mencari ide baru, mengikuti tren, membuat referensi, dan mengembangkan project kreatif sederhana."
}

def score_job(education, competitions, selected_hard, selected_soft, job):
    hard_match = [s for s in job["required_hard"] if s in selected_hard]
    soft_match = [s for s in job["required_soft"] if s in selected_soft]
    competition_match = [c for c in competitions if c in job["preferred_competition"]]

    hard_score = (len(hard_match) / len(job["required_hard"])) * 45
    soft_score = (len(soft_match) / len(job["required_soft"])) * 30
    edu_score = 15 if education in job["education"] else 0
    comp_score = 10 if competition_match else 0

    score = min(100, int(hard_score + soft_score + edu_score + comp_score))

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
    col1, col2 = st.columns([1, 1.25])

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
        fitur_col, tujuan_col = st.columns(2)

        with fitur_col:
            st.markdown("""
            <div class="card">
                <h3>Fitur Sistem</h3>
                <div class="info"><b>🎓 Analisis Pendidikan</b><br>Menyesuaikan rekomendasi pekerjaan dengan jenjang pendidikan pengguna.</div>
                <div class="info"><b>🏆 Analisis Lomba</b><br>Menghitung pengalaman lomba atau prestasi yang relevan dengan bidang pekerjaan.</div>
                <div class="info"><b>🧠 Skill Matching</b><br>Mencocokkan hard skill dan soft skill pengguna dengan kebutuhan setiap pekerjaan.</div>
                <div class="info"><b>📚 Roadmap Belajar</b><br>Memberikan saran pengembangan berdasarkan skill gap yang ditemukan.</div>
            </div>
            """, unsafe_allow_html=True)

        with tujuan_col:
            st.markdown("""
            <div class="card">
                <h3>Tujuan Sistem</h3>
                <div class="info"><b>🎯 Mengenali Career Path</b><br>Membantu pengguna memahami pekerjaan yang paling sesuai dengan profilnya.</div>
                <div class="info"><b>📊 Rekomendasi Berbasis Analisis</b><br>Memberikan hasil berdasarkan kecocokan antara profil pengguna dan kebutuhan pekerjaan.</div>
                <div class="info"><b>📌 Mengetahui Skill Gap</b><br>Menampilkan skill yang sudah sesuai dan skill yang masih perlu dikembangkan.</div>
                <div class="info"><b>🚀 Mendukung Kesiapan Karier</b><br>Memberi arahan agar pengguna lebih siap menghadapi dunia kerja.</div>
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
    selected_hard = st.multiselect("Hard skill yang kamu miliki", hard_skills, placeholder="Pilih hard skill kamu")
    selected_soft = st.multiselect("Soft skill yang kamu miliki", soft_skills, placeholder="Pilih soft skill kamu")

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
        <a class="glints-btn" href="{best['glints_link']}" target="_blank">Cari Lowongan di Glints</a>
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

    if matched_all:
        for s in matched_all:
            st.markdown(f'<span class="good">{s}</span>', unsafe_allow_html=True)
    else:
        st.info("Belum ada skill yang cocok dengan pekerjaan utama.")

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
    else:
        st.markdown("""
        <div class="info">
            <b>Profil sudah kuat</b><br>
            Kamu sudah memenuhi skill utama untuk pekerjaan ini. Selanjutnya, tingkatkan portfolio, buat project nyata, dan siapkan CV yang relevan.
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
            <a class="glints-btn" href="{item['glints_link']}" target="_blank">Lihat di Glints</a>
        </div>
        """, unsafe_allow_html=True)

        st.progress(item["score"] / 100)
