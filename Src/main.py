import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Konfigurasi Halaman Streamlit ---
st.set_page_config(
    page_title="Analisis Kesehatan Mental Siswa",
    page_icon="🧠",
    layout="wide"
)

# --- Fungsi untuk Memuat Data ---
# --- Path untuk dataset --- 
path_data = os.path.abspath("Dataset/StudentMentalHealth.csv") # copy from dataset

@st.cache_data
def load_data():
    df = pd.DataFrame() # Inisialisasi df kosong
    try:
        df = pd.read_csv(path_data)
        
        # --- Pra-pemrosesan Data (tetap di sini) ---
        df.dropna(inplace=True)

        stress_order = ['Low', 'Medium', 'High']
        df['Stress Level'] = pd.Categorical(df['Stress Level'], categories=stress_order, ordered=True)

        bins = [0, 2, 5, df['Physical Activity (hrs/week)'].max() + 1]
        labels = ['Low', 'Medium', 'High']
        df['Physical Activity Category'] = pd.cut(df['Physical Activity (hrs/week)'], bins=bins, labels=labels, right=False)
        physical_activity_order = ['Low', 'Medium', 'High']
        df['Physical Activity Category'] = pd.Categorical(df['Physical Activity Category'], categories=physical_activity_order, ordered=True)

    except FileNotFoundError:
        st.error("Error: File 'StudentMentalHealt.csv' tidak ditemukan di folder 'Dataset/'.")
        st.info("Menggunakan data dummy untuk demonstrasi.")
        # --- Data Dummy (untuk pengembangan jika file tidak ada) ---
        data = {
            'Name': ['Student A', 'Student B', 'Student C', 'Student D', 'Student E', 'Student F', 'Student G', 'Student H', 'Student I', 'Student J'],
            'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
            'Age': [18, 19, 20, 18, 21, 19, 22, 20, 18, 19],
            'Education Level': ['BTech', 'MSc', 'Class 8', 'BTech', 'MSc', 'Class 8', 'BTech', 'MSc', 'Class 8', 'BTech'],
            'Screen Time (hrs/day)': [8, 10, 5, 9, 7, 6, 11, 8, 7, 9],
            'Sleep Duration (hrs)': [7, 6, 8, 7, 5, 7, 6, 8, 7, 6],
            'Physical Activity (hrs/week)': [3, 2, 5, 4, 1, 3, 2, 4, 5, 1],
            'Stress Level': ['Medium', 'High', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High'],
            'Anxious Before Exams': ['Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes'],
            'Academic Performance Change': ['Decreased', 'Decreased', 'Increased', 'Decreased', 'No Change', 'Increased', 'Decreased', 'No Change', 'Increased', 'Decreased']
        }
        df = pd.DataFrame(data) # Assign df dengan data dummy
        
        # Lakukan pra-pemrosesan juga untuk data dummy agar konsisten
        df.dropna(inplace=True)
        stress_order = ['Low', 'Medium', 'High']
        df['Stress Level'] = pd.Categorical(df['Stress Level'], categories=stress_order, ordered=True)
        bins = [0, 2, 5, df['Physical Activity (hrs/week)'].max() + 1]
        labels = ['Low', 'Medium', 'High']
        df['Physical Activity Category'] = pd.cut(df['Physical Activity (hrs/week)'], bins=bins, labels=labels, right=False)
        physical_activity_order = ['Low', 'Medium', 'High']
        df['Physical Activity Category'] = pd.Categorical(df['Physical Activity Category'], categories=physical_activity_order, ordered=True)
    return df # Pastikan df selalu dikembalikan

df = load_data()

# --- Judul Dashboard ---
st.title("🧠 Analisis Kesehatan Mental Siswa Selama Pembelajaran Online")
st.markdown("""
Dashboard ini menyajikan analisis data kesehatan mental siswa selama periode pembelajaran online,
mengungkapkan pola dan hubungan antara faktor demografi, kebiasaan, dan tingkat kesehatan mental.
""")

st.markdown("---")

# --- Sidebar untuk Filter ---
st.sidebar.header("Filter Data")

# Filter Gender
selected_gender = st.sidebar.multiselect(
    "Pilih Jenis Kelamin:",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

# Filter Education Level
selected_education = st.sidebar.multiselect(
    "Pilih Jenjang Pendidikan:",
    options=df['Education Level'].unique(),
    default=df['Education Level'].unique()
)

# Filter Stres Level
selected_stress = st.sidebar.multiselect(
    "Pilih Tingkat Stres:",
    options=df['Stress Level'].cat.categories.tolist(), # Mengambil dari kategori ordered
    default=df['Stress Level'].cat.categories.tolist()
)

# Filter data berdasarkan pilihan sidebar
filtered_df = df[
    (df['Gender'].isin(selected_gender)) &
    (df['Education Level'].isin(selected_education)) &
    (df['Stress Level'].isin(selected_stress))
]

if filtered_df.empty:
    st.warning("Tidak ada data yang tersedia untuk kombinasi filter yang dipilih.")
    st.stop() # Hentikan eksekusi jika tidak ada data

# --- Tampilan Data (Opsional) ---
if st.checkbox("Tampilkan Data Mentah (Filtered)"):
    st.subheader("Data Mentah (Filtered)")
    st.dataframe(filtered_df)

st.markdown("---")

# --- Bagian Analisis dan Visualisasi ---

# --- Visualisasi 1: Distribusi Tingkat Stres Keseluruhan (atau Filtered) ---
st.header("1. Distribusi Tingkat Stres Siswa")
col1, col2 = st.columns([2, 1]) # Membagi layout menjadi 2 kolom: grafik dan penjelasan

with col1:
    stress_dist_data = filtered_df['Stress Level'].value_counts(normalize=True).reset_index()
    fig_stress_dist = px.bar(
        stress_dist_data,
        x='Stress Level',
        y='proportion',
        title='Distribusi Tingkat Stres Siswa',
        labels={'proportion': 'Proporsi Siswa', 'Stress Level': 'Tingkat Stres'},
        text_auto='.1%',
        color='Stress Level',
        category_orders={'Stress Level': df['Stress Level'].cat.categories.tolist()}
    )
    fig_stress_dist.update_layout(xaxis={'categoryorder':'array', 'categoryarray':df['Stress Level'].cat.categories.tolist()})
    st.plotly_chart(fig_stress_dist, use_container_width=True)

with col2:
    st.markdown("""
    Visualisasi ini menampilkan proporsi siswa di setiap kategori tingkat stres (*Low, Medium, High*)
    berdasarkan filter yang dipilih. Ini memberikan gambaran umum tentang seberapa parah tingkat stres
    yang dilaporkan oleh siswa dalam kelompok yang diamati.

    * **Temuan:** 
    	- Mayoritas siswa berada pada tingkat **stres sedang**, dengan persentase sekitar **49%**.
		- Tingkat **stres rendah** menempati urutan kedua dengan persentase **32,7%**.
		- Sementara itu, sekitar **18%** siswa mengalami **stres tinggi**.
    * **Implikasi:**
    	- Data ini menunjukkan bahwa hampir **setengah dari siswa yang terdata mengalami stres sedang**, yang menandakan adanya tekanan psikologis yang cukup signifikan, meskipun belum mencapai kategori berat.
		- Sekitar **32,7% siswa berada pada tingkat stres rendah**, yang dapat diinterpretasikan sebagai kelompok dengan **kesehatan mental yang relatif stabil dan dalam kondisi aman**.
		- Meskipun jumlahnya lebih kecil, **sekitar 181 siswa atau 18% dari total** mengalami **tingkat stres tinggi**, yang mengindikasikan perlunya **perhatian dan intervensi lebih lanjut** untuk kelompok ini agar tidak berkembang menjadi gangguan mental yang lebih serius.
    """)

st.markdown("---")

# --- Visualisasi 2: Tingkat Stres Berdasarkan Jenis Kelamin ---
st.header("2. Tingkat Stres Berdasarkan Jenis Kelamin")
col1, col2 = st.columns([2, 1])

with col1:
    fig_gender_stress = px.histogram(
        filtered_df,
        x='Stress Level',
        color='Gender',
        title='Distribusi Tingkat Stres Berdasarkan Jenis Kelamin',
        labels={'Stress Level': 'Tingkat Stres', 'Gender': 'Jenis Kelamin'},
        barmode='group',
        category_orders={'Stress Level': df['Stress Level'].cat.categories.tolist()}
    )
    st.plotly_chart(fig_gender_stress, use_container_width=True)

with col2:
    st.markdown("""
    Grafik ini membandingkan distribusi tingkat stres antara siswa laki-laki dan perempuan.
    Ini membantu kita melihat apakah ada disparitas kesehatan mental berdasarkan gender.

    * **Temuan:**
	- **Tingkat stres pada laki-laki** 
		- tingkat stress rendah: 32,6%
		- tingkat stress menengah: 50,3%
		- tingkat stress rendah: 17,1%
	- **Tingkat stres pada perempuan** 
		- tingkat stress rendah: 33,1%
		- tingkat stress menengah: 49,1%
		- tingkat stress rendah: 17,8%
    
    * **Implikasi:** 
	- **Siswa dengan tingkat stres paling rendah** adalah laki-laki dengan dengan selisih 0,5% lebih sdeikit di bandingkan siswa perempuan.
	- Menariknya, **siswa dengan tingkat stres menengah juga laki-laki dimana terdapat selisih 1,2% lebih banyak siswa laki-laki** dibandingkan dengan perempuan.
	- Namun, **siswa dengan tingkat stres tinggi ter banyak adalah perempuan dimana terdapat selisih 0,7% lebih banyak siswa perempuan** yang mengalami stress tinggi dibandingkan laki-laki.
    """)

st.markdown("---")

# --- Visualisasi 3: Durasi Tidur Berdasarkan Tingkat Stres ---
st.header("3. Durasi Tidur Berdasarkan Tingkat Stres")
col1, col2 = st.columns([2, 1])

with col1:
    fig_sleep_stress = px.box(
        filtered_df,
        x='Stress Level',
        y='Sleep Duration (hrs)',
        title='Distribusi Durasi Tidur Berdasarkan Tingkat Stres',
        labels={'Stress Level': 'Tingkat Stres', 'Sleep Duration (hrs)': 'Durasi Tidur (Jam)'},
        color='Stress Level',
        category_orders={'Stress Level': df['Stress Level'].cat.categories.tolist()}
    )
    st.plotly_chart(fig_sleep_stress, use_container_width=True)

with col2:
    st.markdown("""
    Box plot ini menunjukkan distribusi durasi tidur siswa untuk setiap kategori tingkat stres.
    Kita bisa melihat median durasi tidur, rentang interkuartil, dan keberadaan outlier.

    * **Temuan:** 
		- **Stres Rendah:**
			- Q1 (kuartil bawah): 5,1 jam
			- Q2 (median): 6,6 jam
			- Q3 (kuartil atas): 7,8 jam

		- **Stres Sedang:**
			- Q1: 5,2 jam
			- Q2: 6,4 jam
			- Q3: 7,6 jam

		- **Stres Tinggi:**
			- Q1: 5,15 jam
			- Q2: 6,5 jam
			- Q3: 7,7 jam

    * **Implikasi:** 
		- Data menunjukkan bahwa **tingkat stres memengaruhi pola tidur siswa**.
		- **Siswa dengan tingkat stres rendah** cenderung tidur lebih lama — sekitar **10% lebih banyak** dibandingkan dengan siswa yang mengalami stres tinggi.
		- Menariknya, **siswa dengan tingkat stres sedang justru memiliki durasi tidur yang lebih pendek** dibandingkan baik kelompok stres rendah maupun stres tinggi.
		- Hal ini bisa mengindikasikan bahwa pada tingkat stres sedang, siswa mungkin mengalami **gangguan tidur yang tidak stabil**, seperti sulit tidur meskipun tidak dalam tekanan ekstrem.
    """)

st.markdown("---")

# --- Visualisasi 4: Tingkat Kecemasan Sebelum Ujian Berdasarkan Jenjang Pendidikan ---
st.header("4. Tingkat Kecemasan Sebelum Ujian Berdasarkan Jenjang Pendidikan")
col1, col2 = st.columns([2, 1])

with col1:
    # Agregasi data untuk proporsi
    anxious_edu_data = filtered_df.groupby('Education Level')['Anxious Before Exams'].value_counts(normalize=True).unstack().fillna(0).reset_index()
    
    # Pastikan kolom 'Yes' dan 'No' ada
    cols_to_plot = []
    if 'Yes' in anxious_edu_data.columns:
        cols_to_plot.append('Yes')
    if 'No' in anxious_edu_data.columns:
        cols_to_plot.append('No')

    if cols_to_plot:
        fig_edu_anxious = px.bar(
            anxious_edu_data,
            x='Education Level',
            y=cols_to_plot,
            title='Proporsi Siswa Cemas Sebelum Ujian Berdasarkan Jenjang Pendidikan',
            labels={'value': 'Proporsi', 'variable': 'Jawaban Kecemasan'},
            barmode='group',
            height=500
        )
        fig_edu_anxious.update_layout(yaxis_tickformat='.0%')
        st.plotly_chart(fig_edu_anxious, use_container_width=True)
    else:
        st.info("Tidak ada data 'Yes' atau 'No' untuk kecemasan ujian berdasarkan filter.")

with col2:
    st.markdown("""
    Grafik ini menampilkan proporsi siswa yang merasa cemas atau tidak cemas sebelum ujian,
    dibagi berdasarkan jenjang pendidikan mereka.

    * **Temuan:** 
    #### 📌 Jenjang Bachelor (S1)
		- Mayoritas siswa pada jenjang **S1** menunjukkan **tingkat kecemasan yang paling tinggi** sebelum ujian.
		- Rata-rata persentase siswa yang menyatakan _"Ya, cemas"_ berada di angka **58%**.
		- Sebaran data lebih terkonsentrasi pada nilai-nilai tinggi.

	#### 📌 Jenjang Kelas 8-12
		- Siswa di jenjang ini menunjukkan **variasi tingkat kecemasan yang lebih seimbang**.
		- Proporsi yang menjawab _"Ya, cemas"_ berkisar antara **46–50%**.
		- Yang menjawab _"Tidak cemas"_ sedikit lebih tinggi, yaitu **51–54%**.
		- Hal ini mengindikasikan adanya **keseimbangan antara siswa yang merasa cemas dan tidak cemas**.

	#### 📌 Jenjang Magister (S2)
		- Tingkat kecemasan pada jenjang **S2** terlihat lebih **bervariasi**.
		- Kemungkinan besar dipengaruhi oleh faktor-faktor lain seperti **jurusan atau pengalaman individu**.

    
    * **Implikasi:** 
	- **Jenjang S1** menonjol sebagai kelompok dengan tingkat kecemasan tertinggi (**56–60%** menjawab "Ya, cemas").  
		Hal ini mungkin disebabkan oleh:
		- Tekanan akademik yang lebih intens.
		- Ketergantungan kuat pada hasil ujian untuk kelulusan atau karier.
	- **Kelas 11** menunjukkan **keseimbangan antara kecemasan dan ketenangan**, menjadikannya titik fokus yang baik untuk intervensi jika diperlukan.
	- **Kelas 8**
		memiliki tingkat kecemasan terendah, dengan **54% menyatakan "Tidak cemas"**.Ini bisa jadi karena:
		- Mereka belum terlalu terbebani ekspektasi atau dampak besar dari hasil ujian.
	- **Mahasiswa Magister (S2)** 
 		cenderung memiliki **strategi manajemen stres yang lebih baik**, sehingga tingkat kecemasan lebih tergantung pada faktor lain seperti dinamika jurusan.

    """)

st.markdown("---")

# --- Visualisasi 5: Perubahan Performa Akademik Berdasarkan Tingkat Stres ---
st.header("5. Perubahan Tingkat Stres Berdasarkan intensitas aktivitas fisik")
col1, col2 = st.columns([2, 1])

with col1:
    fig_perf_stress = px.histogram(
        filtered_df,
        x='Stress Level',
        color='Physical Activity Category',
        title='Perubahan Tingkat Stress berdasar intensitas Aktivitas fisik',
        labels={'Physical Activity Category': 'Kategori Aktivitas Fisik', 'Stress Level': 'Tingkat Stres'},
        category_orders={'Physical Activity Category': df['Physical Activity Category'].cat.categories.tolist(),
                        'Stress Level': df['Stress Level'].cat.categories.tolist()},
        barmode='group',
        height=500
    )
    st.plotly_chart(fig_perf_stress, use_container_width=True)

with col2:
    st.markdown("""
    Visualisasi ini mengeksplorasi hubungan antara tingkat stres siswa dan intensitas aktivitas fisik yang dilakukan dengan pengkategorian
	- **0 - 2 jam** → *Low* (Rendah)
	- **2 - 4 jam** → *Medium* (Sedang)
	- **> 4 jam** → *High* (Tinggi)

    ##### **Temuan Utama:**
		- **Siswa dengan tingkat stres rendah** paling banyak melakukan aktivitas fisik dengan intensitas *tinggi* (57,1%), diikuti oleh *sedang* (21%), dan *rendah* (20,9%).
		- **Siswa dengan tingkat stres sedang** tercatat 59,1% berada pada kategori aktivitas *tinggi*, 23,1% *sedang*, dan 17,8% *rendah*.
		- **Siswa dengan tingkat stres tinggi** justru memiliki proporsi aktivitas fisik *tinggi* yang lebih besar lagi yaitu 64%, diikuti oleh *sedang* (18,7%) dan *rendah* (17,3%).

    * **Implikasi:** Data ini menunjukkan bahwa **aktivitas fisik memang berkaitan dengan tingkat stres**, tetapi hubungan tersebut **tidak selalu linier**. Beberapa poin penting yang bisa disimpulkan:
		- **Aktivitas fisik yang tinggi tidak selalu identik dengan tingkat stres yang rendah.** Misalnya, siswa dengan stres tinggi justru memiliki proporsi aktivitas fisik tinggi sebesar **64%**, lebih tinggi dibandingkan siswa dengan stres rendah (**57,1%**).
		- **Siswa dengan stres rendah memiliki distribusi aktivitas fisik yang lebih seimbang**, terutama pada kategori aktivitas sedang (**21%**), dibandingkan dengan siswa yang mengalami stres tinggi (**17,3%**). Ini mengindikasikan bahwa **aktivitas fisik dengan intensitas sedang mungkin lebih efektif dalam menjaga keseimbangan mental**.
		- Aktivitas fisik **berlebihan** (terlalu tinggi) juga bisa menjadi beban tambahan dan justru meningkatkan stres, tergantung pada konteks dan kemampuan fisik siswa.
    """)

st.markdown("---")

# --- Kesimpulan dan Rekomendasi (Singkat untuk Dashboard) ---
st.header("Kesimpulan dan Rekomendasi Awal")
st.markdown("""
Dari analisis ini, terlihat bahwa kesehatan mental siswa selama pembelajaran online dipengaruhi
oleh berbagai faktor demografi dan kebiasaan. Tingkat stres dan kecemasan adalah isu yang signifikan
bagi banyak siswa, dan ada hubungan yang jelas antara kebiasaan tidur, aktivitas fisik, dan tingkat stres.

**Rekomendasi Awal:**
* **Program Dukungan Kesehatan Mental:** Mengembangkan program yang ditargetkan, terutama untuk
    jenjang pendidikan yang menunjukkan tingkat stres dan kecemasan tinggi (misalnya, siswa S1).
* **Peningkatan Kesadaran:** Mengedukasi siswa tentang pentingnya durasi tidur yang cukup dan
    aktivitas fisik yang teratur sebagai bagian dari manajemen stres.
* **Dukungan Ujian:** Memberikan strategi penanganan kecemasan sebelum ujian, terutama bagi
    kelompok yang paling rentan.
""")

st.markdown("---")
