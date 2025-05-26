# Analysis-MentalHealth-StudentOnlineLearning

## Judul Proyek: Analisis Kesehatan Mental Siswa Selama Pembelajaran Online
### 1. Pendahuluan
- Latar Belakang: Kesehatan mental siswa selama pembelajaran sangatlah penting bagi siswa, baik untuk memahami materi yang dipelajari ataupun mengimplementasikannya di dunia nyata.
- Tujuan Proyek: Menganalisis dampak pembelajaran online terhadap kesehatan mental siswa, mengidentifikasi faktor-faktor yang memengaruhi, dan memberikan insight untuk intervensi.
- Sumber Data: Dataset yang digunakan berasal dari ( https://www.kaggle.com/datasets/utkarshsharma11r/student-mental-health-analysis?resource=download ) Kumpulan data ini berisi tanggapan dari siswa mengenai status kesehatan mental mereka selama era pembelajaran daring. Kumpulan data tersebut terdiri dari 1.000 entri dan 10 kolom.

---

### 2. Pemahaman dan Pembersihan Data (Data Understanding & Cleaning)
Dataset ini adalah dataset yang sudah jadi artinya kita dapat langsung menggunakanya tanapa perlu melakukan tahap pembersihan seperti dataset biasanya oleh karena itu dalam proses ini kita tidak melakukan proses pembersihan pada dataset

#### **Gambaran Umum Dataset:**
Kumpulan data ini berisi tanggapan dari siswa mengenai status kesehatan mental mereka selama era pembelajaran daring. Data dikumpulkan melalui survei dan berfokus pada berbagai aspek psikologis dan perilaku yang dipengaruhi oleh pendidikan jarak jauh. 
Kumpulan data dapat digunakan untuk analisis data eksploratif (EDA), visualisasi data, dan pemodelan prediktif untuk lebih memahami bagaimana pendidikan daring memengaruhi kesejahteraan mental siswa. 
Berikut ringkasan kolom dan tujuannya:
- | Nama Nama depan siswa (tidak penting untuk analisis; dapat dianonimkan)
- | Jenis Kelamin Jenis Kelamin Responden (Pria/Wanita)
- | Usia Usia dalam tahun
- | Tingkat Pendidikan Tingkat akademis (misalnya, Kelas 8, BTech, MSc)
- | Waktu Layar (jam/hari) Rata-rata waktu layar per hari selama pembelajaran daring
- | Durasi Tidur (jam) Rata-rata durasi tidur harian
- | Aktivitas Fisik (jam/minggu) Waktu latihan mingguan
- | Tingkat Stres Tingkat stres yang dilaporkan (Rendah, Sedang, Tinggi)
- | Cemas Sebelum Ujian Apakah siswa merasa cemas sebelum ujian (Ya/Tidak)
- | Perubahan Kinerja Akademik Perubahan yang dinilai sendiri dalam kinerja akademik

---

### 3. Analisis Data Eksploratif (EDA) & Visualisasi
Ini adalah bagian inti tempat kamu menyajikan temuan dan grafik. Untuk setiap pertanyaan analisis yang kamu pilih, buat sub-bagian terpisah.

#### 3.1. Pertanyaan Analisis 1: [1. Profil Umum Kesehatan Mental Siswa Berdasarkan Demografi]
#### Tujuan: Memahami bagaimana distribusi tingkat stres, durasi tidur, dan kecemasan sebelum ujian di kalangan siswa secara - keseluruhan, dan apakah ada pola yang berbeda berdasarkan jenis kelamin atau jenjang pendidikan.
**Pertanyaan Kunci:**
- Bagaimana proporsi siswa di setiap kategori tingkat stres (Low, Medium, High)?
- Apakah ada perbedaan signifikan dalam tingkat stres, durasi tidur atau kecemasan sebelum ujian di berbagai jenjang pendidikan?
- Apakah ada variasi dalam indikator kesehatan mental ini di berbagai jenjang pendidikan?

##### Judul 3.1.1[Distribusi Keseluruhan Tingkat Stres]:
Visualisasi:(visualizations/output_charts/nama_file_gambar.png))
Temuan Utama: 
- Mayoritas siswa berada pada tingkat **stres sedang**, dengan persentase sekitar **49%**.
- Tingkat **stres rendah** menempati urutan kedua dengan persentase **32,7%**.
- Sementara itu, sekitar **18%** siswa mengalami **stres tinggi**
  
Implikasi: 

- Data ini menunjukkan bahwa hampir **setengah dari siswa yang terdata mengalami stres sedang**, yang menandakan adanya tekanan psikologis yang cukup signifikan, meskipun belum mencapai kategori berat.
- Sekitar **32,7% siswa berada pada tingkat stres rendah**, yang dapat diinterpretasikan sebagai kelompok dengan **kesehatan mental yang relatif stabil dan dalam kondisi aman**.
- Meskipun jumlahnya lebih kecil, **sekitar 181 siswa atau 18% dari total** mengalami **tingkat stres tinggi**, yang mengindikasikan perlunya **perhatian dan intervensi lebih lanjut** untuk kelompok ini agar tidak berkembang menjadi gangguan mental yang lebih serius.

---

##### Judul 3.1.2[Distribusi Tingkat Stres di Setiap Jenjang Pendidikan]:
(Sisipkan gambar grafik di sini)
Temuan Utama:
- **Jenjang Magister (S2)** menunjukkan tingkat stres **sedang** yang cukup tinggi, yaitu antara **45–60%**. Namun, variasi tingkat stres ini juga bergantung pada **program studi** yang diambil:
  - Beberapa program studi menunjukkan tingkat stres **rendah** sekitar **40–45%**.
  - Tingkat stres **tinggi** pada jenjang ini relatif rendah, berada di kisaran **15–25%**.
- **Siswa Kelas 9–11** memiliki rata-rata tingkat stres **sedang** yang lebih tinggi dibandingkan dengan siswa jenjang **Bachelor (S1)**.
- Meskipun demikian, rata-rata tingkat **stres tinggi** lebih banyak dialami oleh siswa jenjang **S1** dibandingkan siswa Kelas 9–11.
- **Siswa Kelas 8 dan 12** menunjukkan rata-rata tingkat stres (rendah, sedang, dan tinggi) yang **cenderung paling rendah** di antara semua jenjang pendidikan.

Implikasi: 
- Data ini menunjukkan bahwa **jenjang pendidikan memiliki pengaruh terhadap tingkat stres siswa**, namun faktor **jurusan atau program studi** juga berperan penting.
- Contohnya:
  - Di jenjang **Magister (S2)**:
    - Siswa **MTech** memiliki tingkat stres **sedang** yang lebih tinggi dibandingkan **MA** dan **MSc**.
    - Namun, siswa **MA** dan **MSc** justru memiliki tingkat stres **tinggi** yang lebih besar dibandingkan **MTech**.
  - Di jenjang **Bachelor (S1)**:
    - Siswa **BSc** memiliki tingkat stres **sedang** yang lebih tinggi dibandingkan **BTech** dan **BA**.
    - Sebaliknya, tingkat stres **tinggi** lebih banyak dialami oleh siswa **BTech** dan **BA** dibandingkan **BSc**.

---

##### Judul 3.1.3[Analisis Tingkat Kecemasan Siswa Sebelum Ujian Berdasarkan Jenjang Pendidikan]:

Temuan utama: 
#### 📌 Jenjang Sarjana (S1)
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

Implikasi: Data ini dengan jelas menunjukkan adanya **hubungan antara jenjang pendidikan dan tingkat kecemasan siswa** sebelum ujian.
- **Jenjang S1** menonjol sebagai kelompok dengan tingkat kecemasan tertinggi (**56–60%** menjawab "Ya, cemas").  
  Hal ini mungkin disebabkan oleh:
  - Tekanan akademik yang lebih intens.
  - Ketergantungan kuat pada hasil ujian untuk kelulusan atau karier.
- **Kelas 11** menunjukkan **keseimbangan antara kecemasan dan ketenangan**, menjadikannya titik fokus yang baik untuk intervensi jika diperlukan.
- **Kelas 8** memiliki tingkat kecemasan terendah, dengan **54% menyatakan "Tidak cemas"**.  
  Ini bisa jadi karena:
  - Mereka belum terlalu terbebani ekspektasi atau dampak besar dari hasil ujian.
- **Mahasiswa Magister (S2)** cenderung memiliki **strategi manajemen stres yang lebih baik**, sehingga tingkat kecemasan lebih tergantung pada faktor lain seperti dinamika jurusan.

---

##### Judul 3.1.4[Durasi Tidur Berdasarkan Tingkat Stres]:

Temuan utama: Rata-rata Durasi tidur pada setiap kategori tingkat stres dapat dijelaskan sebagai berikut:

- **Stres Rendah:**
  - Q1 : 5,1 jam
  - Q2 : 6,6 jam
  - Q3 : 7,8 jam

- **Stres Sedang:**
  - Q1: 5,2 jam
  - Q2: 6,4 jam
  - Q3: 7,6 jam

- **Stres Tinggi:**
  - Q1: 5,15 jam
  - Q2: 6,5 jam
  - Q3: 7,7 jam

Implikasi:
- Data menunjukkan bahwa **tingkat stres memengaruhi pola tidur siswa**.
- **Siswa dengan tingkat stres rendah** cenderung tidur lebih lama — sekitar **10% lebih banyak** dibandingkan dengan siswa yang mengalami stres tinggi.
- Menariknya, **siswa dengan tingkat stres sedang justru memiliki durasi tidur yang lebih pendek** dibandingkan baik kelompok stres rendah maupun stres tinggi.
- Hal ini bisa mengindikasikan bahwa pada tingkat stres sedang, siswa mungkin mengalami **gangguan tidur yang tidak stabil**, seperti sulit tidur meskipun tidak dalam tekanan ekstrem.

---

#### 3.2. Pertanyaan Analisis 2: [Dampak Kebiasaan Harian terhadap Kesehatan Mental]
#### Tujuan Analisis: Menjelajahi hubungan antara kebiasaan gaya hidup siswa (waktu layar, durasi tidur, aktivitas fisik) dengan tingkat stres dan kecemasan mereka.
Pertanyaan Kunci:
- Bagaimana waktu layar (Screen Time) yang tinggi berkaitan dengan tingkat stres? Apakah siswa dengan waktu layar lebih tinggi cenderung memiliki tingkat stres yang lebih tinggi?
- Apakah durasi tidur (Sleep Duration) yang lebih panjang berhubungan dengan tingkat stres yang lebih rendah atau kurangnya kecemasan sebelum ujian?
- Apakah aktivitas fisik (Physical Activity) yang lebih banyak berkorelasi dengan tingkat stres yang lebih rendah atau performa akademik yang lebih stabil?

##### Judul 3.1.1[Tingkat Stres Siswa Berdasarkan Aktivitas Penggunaan Gadget]:
**Kategori Penggunaan Gadget:**
- **0 - 4,5 jam** → *Low* (Rendah)
- **4,6 - 8,5 jam** → *Medium* (Sedang)
- **> 8,5 jam** → *High* (Tinggi)



Temuan Utama:
- **Tingkat stres rendah** paling banyak ditemukan pada siswa yang menggunakan gadget dalam rentang waktu *sedang* (42,8%), diikuti oleh rentang *tinggi* (32,7%).
- **Tingkat stres sedang** juga didominasi oleh penggunaan gadget dalam rentang *sedang* (42,2%), dan *tinggi* (32,5%).
- **Tingkat stres tinggi** menunjukkan distribusi yang sedikit berbeda: 37% menggunakan gadget dalam durasi *sedang* maupun *tinggi*, sedangkan 26% berada pada kategori *rendah*.

Implikasi:
Data menunjukkan adanya **keterkaitan antara tingkat stres siswa dan durasi penggunaan gadget**. Beberapa poin penting:
- Siswa dengan **tingkat stres tinggi cenderung memiliki penggunaan gadget yang lebih rendah** dibandingkan siswa dengan stres sedang atau rendah. Misalnya, hanya **37%** dari siswa dengan stres tinggi berada pada kategori *penggunaan sedang*, lebih rendah dibandingkan dengan **42,2%** (stres sedang) dan **42,8%** (stres rendah).
- Namun, siswa dengan **tingkat stres tinggi juga menunjukkan proporsi penggunaan gadget dalam durasi panjang (tinggi) sebesar 37%**, yang **lebih tinggi 4%** dibandingkan siswa dengan stres rendah maupun sedang.
- Dari sisi sebaliknya, **penggunaan gadget juga berpotensi memengaruhi tingkat stres**. Siswa dengan **penggunaan gadget rendah** cenderung memiliki tingkat stres yang lebih rendah. Contohnya, **24,5% siswa dengan stres rendah** berada pada kategori penggunaan gadget rendah, hanya sedikit di bawah **26% siswa dengan stres tinggi**.
---

##### Judul 3.1.2[Tingkat Stres Siswa Berdasarkan Aktivitas Fisik yang Dilakukan]:
**Kategori Durasi Aktivitas Fisik per Hari:**
- **0 - 2 jam** → *Low* (Rendah)
- **2 - 4 jam** → *Medium* (Sedang)
- **> 4 jam** → *High* (Tinggi)



Temuan Utama:
- **Siswa dengan tingkat stres rendah** paling banyak melakukan aktivitas fisik dengan intensitas *tinggi* (57,1%), diikuti oleh *sedang* (21%), dan *rendah* (20,9%).
- **Siswa dengan tingkat stres sedang** tercatat 59,1% berada pada kategori aktivitas *tinggi*, 23,1% *sedang*, dan 17,8% *rendah*.
- **Siswa dengan tingkat stres tinggi** justru memiliki proporsi aktivitas fisik *tinggi* yang lebih besar lagi yaitu 64%, diikuti oleh *sedang* (18,7%) dan *rendah* (17,3%).

Implikasi: Data ini menunjukkan bahwa **aktivitas fisik memang berkaitan dengan tingkat stres**, tetapi hubungan tersebut **tidak selalu linier**. Beberapa poin penting yang bisa disimpulkan:
- **Aktivitas fisik yang tinggi tidak selalu identik dengan tingkat stres yang rendah.** Misalnya, siswa dengan stres tinggi justru memiliki proporsi aktivitas fisik tinggi sebesar **64%**, lebih tinggi dibandingkan siswa dengan stres rendah (**57,1%**).
- **Siswa dengan stres rendah memiliki distribusi aktivitas fisik yang lebih seimbang**, terutama pada kategori aktivitas sedang (**21%**), dibandingkan dengan siswa yang mengalami stres tinggi (**17,3%**). Ini mengindikasikan bahwa **aktivitas fisik dengan intensitas sedang mungkin lebih efektif dalam menjaga keseimbangan mental**.
- Aktivitas fisik **berlebihan** (terlalu tinggi) juga bisa menjadi beban tambahan dan justru meningkatkan stres, tergantung pada konteks dan kemampuan fisik siswa.
---

##### Judul 3.1.3[Hubungan antara durasi tidur berdasarkan jenis kelamin dan tingkat stress berdasarkan durasi tidur]:




Temuan Utama:
- **Laki-laki:**
  - Q1 : 5,1 jam
  - Q2 : 6,5 jam
  - Q3 : 7,8 jam

- **Perempuan:**
  - Q1: 5,1 jam
  - Q2: 6,5 jam
  - Q3: 7,6 jam

- **Tingkat stres pada laki-laki** 
  - tingkat stress rendah: 32,6%
  - tingkat stress menengah: 50,3%
  - tingkat stress rendah: 17,1%
- **Tingkat stres pada perempuan** 
  - tingkat stress rendah: 33,1%
  - tingkat stress menengah: 49,1%
  - tingkat stress rendah: 17,8%

Implikasi: Data menunjukkan bahwa **gender dan durasi tidur mempengaruhi tingkat stres siswa**.
- **Siswa dengan tingkat stres paling rendah** adalah laki-laki dengan durasi tidur pada kuartil tinggi **10% lebih lama** dibandingkan dengan siswa perempuan.
- Menariknya, **siswa dengan tingkat stres menengah juga laki-laki dimana terdapat selisih 1,2% lebih banyak siswa laki-laki** dibandingkan dengan perempuan.
- Namun, **siswa dengan tingkat stres tinggi ter banyak adalah perempuan dimana terdapat selisih 0,7% lebih banyak siswa perempuan** yang mengalami stress tinggi dibandingkan laki-laki.
- Hal ini bisa mengindikasikan bahwa pada tingkat stres pada seorang siswa tidak terlalu di pengaruhi oleh jam tidur namun lebih di pengaruhi oleh gender (jenis kelamin).
---

#### 4. Kesimpulan dan Rekomendasi
Dari analisis ini, terlihat jelas bahwa kesehatan mental siswa selama pembelajaran online dipengaruhi oleh berbagai faktor, meliputi demografi dan kebiasaan sehari-hari. Tingkat stres dan kecemasan adalah isu signifikan bagi banyak siswa, dengan adanya hubungan yang jelas antara kebiasaan tidur, aktivitas fisik, intensitas penggunaan gadget, dan tingkat stres.

Rekomendasi Awal:
- Program Dukungan Kesehatan Mental Terfokus: Mengembangkan program dukungan yang ditargetkan, khususnya untuk jenjang pendidikan yang menunjukkan tingkat stres dan kecemasan tinggi (misalnya, mahasiswa S1).
- Peningkatan Kesadaran Gaya Hidup Sehat: Mengedukasi siswa tentang pentingnya durasi tidur yang cukup dan aktivitas fisik yang teratur sebagai bagian dari manajemen stres.
- Strategi Penanganan Kecemasan Ujian: Memberikan strategi penanganan kecemasan sebelum ujian, terutama bagi kelompok yang paling rentan.

Langkah Selanjutnya:
- Kita dapat mengamati lebih lanjut hubungan antara kinerja akademik (performa akademik) dengan tingkat stres dan kecemasan siswa sebelum ujian.
- Hasil analisis ini dapat dimanfaatkan sebagai modal awal untuk membuat program penanganan stres pada siswa berdasarkan jenjang pendidikan atau kebiasaan siswa, dengan tujuan akhir meningkatkan performa akademis siswa.  

---

#### 5. Struktur Proyek dan Cara Menjalankan
  Analysis_MentalHealth_StudentOnlineLearning/
  |
  ├── Dataset/
  │   └── StudentMentalHealth.csv
  |
  ├── Notebooks/
  │   └── analysis_data.ipynb
  |
  ├── src/
  │   └── main.py
  |
  ├── visualizations/
  │   └── output_charts/
  |
  ├── README.md
  ├── requirements.txt
  └── .gitignore

### **Cara Menjalankan (Set up):**
Kloning Repositori:
Bash
git clone https://github.com/namamu/nama-project-kesehatan-mental-siswa.git
cd nama-project-kesehatan-mental-siswa
Buat dan Aktifkan Virtual Environment:
Bash

#### python -m venv venv
#### Windows: .\venv\Scripts\activate
#### macOS/Linux: source venv/bin/activate

  Instal Dependensi:
  Bash
- pip install -r requirements.txt
  
  Menjalankan Analisis EDA (Jupyter Notebook):
  Bash
- jupyter notebook notebooks/eda_analysis.ipynb
  
  Menjalankan Dashboard Streamlit:
  Bash
- streamlit run Src/main.py

#### 6. Kontak (Opsional)
Jika kamu ingin orang lain bisa menghubungimu.

LinkedIn: [Link Profil LinkedInmu]
GitHub: [Link Profil GitHubmu]
Email: []
