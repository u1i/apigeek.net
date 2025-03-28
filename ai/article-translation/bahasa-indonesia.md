# Kebangkitan Kekuatan AI

Ingat bagaimana GPT dari OpenAI menjadi pilihan default untuk sebagian besar proyek AI? Kini, lanskap AI telah berubah drastis hanya dalam beberapa bulan, dengan raksasa teknologi seperti Meta, Microsoft, Databricks, dan Apple merilis model terbuka mereka sendiri. Mari kita lihat bagaimana era baru pilihan dan aksesibilitas ini mengubah cara kita membangun aplikasi cerdas, mengapa tidak ada solusi satu ukuran untuk semua, dan bagaimana Anda dapat menavigasi lanskap yang berevolusi pesat ini untuk menemukan pendekatan terbaik yang sesuai dengan kebutuhan Anda.

Hingga akhir tahun lalu, ketika ditanya tentang membangun aplikasi cerdas menggunakan AI, saya dengan enggan mengakui bahwa GPT dari OpenAI mungkin satu-satunya opsi yang layak pada saat itu. Itu seperti memiliki kotak peralatan dengan hanya satu alat - atau katakanlah banyak alat canggih, tetapi semuanya dari merek yang sama, dengan batasan dan keanehan yang sama. Saya sangat mengenal keluarga GPT, setelah bekerja dengan GPT-2, GPT-3, dan semua varian .5 dan turbo. Jangan salah, mereka hebat, tetapi seperti yang saya katakan, semuanya dari satu perusahaan. Sebelumnya, saya telah menulis tentang kebutuhan akan rencana B. Apa yang terjadi ketika API model bahasa besar andalan Anda tiba-tiba dihentikan dan diganti dengan yang baru?

## Revolusi Model AI: Munculnya Ekosistem yang Beragam

Namun, hanya dalam beberapa bulan, semuanya berubah. Anthropic dan Google telah merilis model AI canggih yang hampir sama mampunya dengan milik OpenAI. Yang lebih signifikan lagi, raksasa teknologi seperti Meta, Apple, dan Microsoft telah membuat model mereka menjadi open source dan tersedia untuk diunduh. Ini berarti Anda dapat menjalankannya di infrastruktur Anda sendiri alih-alih hanya mengaksesnya melalui API, yang tidak nyaman bagi beberapa orang karena melibatkan pengiriman data Anda ke tempat yang tidak diketahui.

Tiba-tiba, kotak peralatan saya dipenuhi dengan alat-alat baru yang berkilau, masing-masing dengan fitur dan kemampuan uniknya sendiri, dan lanskap model AI telah berubah menjadi ekosistem yang beragam. Beberapa model terbuka baru ini, seperti Llama 3, kini sama kuatnya dengan GPT hanya 1,5 tahun yang lalu, dan beberapa, luar biasa, bahkan dapat berjalan di MacBook Air saya! Rasanya seperti menyaksikan dunia hitam-putih tiba-tiba meledak dengan warna karena AI menjadi lebih mudah diakses dan serbaguna dari sebelumnya. Mari kita lihat beberapa rilis terpenting dari beberapa bulan terakhir.

## Kemajuan Terbaru dalam Model Bahasa Besar

• Google Gemini (6 Desember 2023): Lineup model canggih Google, termasuk versi 1.0, 1.5 (Pro dan Ultra) dengan jendela konteks hingga 1 juta token - saya telah banyak bekerja dengan ini, dan sangat menyukai bagaimana mereka berkembang.

• Mixtral dari Mistral (11 Desember 2023): merilis Mixtral 8x7B, model campuran pakar jarang berkualitas tinggi (SMoE) dengan bobot terbuka yang sesuai atau melampaui GPT3.5 pada sebagian besar tolok ukur standar. Sampai saat itu, saya belum banyak menjelajahi model Mistral.

• Gemma oleh Google (21 Februari 2024): Keluarga model terbuka ringan dan mutakhir yang dibangun dari penelitian dan teknologi yang sama dengan model Gemini Google, menjadikan AI canggih lebih mudah diakses oleh pengembang. Mereka adalah model yang luar biasa kecil, dan ketika saya mencobanya, saya menyadari bahwa untuk beberapa kasus penggunaan, kami hanya membutuhkan mesin yang dapat memahami bahasa dan terlibat dengan pengguna. Sekarang, kami dapat memiliki kemampuan tersebut tertanam dalam perangkat lunak yang dapat saya jalankan di mesin saya sendiri, dan saya tidak perlu bergantung pada OpenAI.

• Anthropic Claude 3 (4 Maret 2024): Penawaran terbaru Anthropic termasuk Haiku, Sonnet, dan Opus, dan saya beruntung memiliki akses penelitian ke model-model ini untuk beberapa waktu. Menurut pendapat saya, mereka adalah alternatif paling kuat untuk model OpenAI saat ini. Khususnya Opus terasa hangat, menarik, dan merupakan model yang luar biasa untuk membangun kepribadian digital yang dapat terlibat dalam percakapan intelektual yang mendalam dan menampilkan kemampuan penalaran tingkat lanjut.

• Grok oleh X (dirilis 18 Maret 2024): Diumumkan sebagai "model bahasa sumber terbuka", perusahaan hanya merilis bobot ke publik, tanpa kode atau banyak dokumentasi, membuat banyak pengembang tidak yakin tentang kemampuan dan kegunaan sebenarnya. Saya ingin mencobanya, tetapi saat ini terlalu besar untuk dijalankan di perangkat keras saya sendiri atau di cloud.

• MM1 oleh Apple (dirilis 19 Maret 2024): model bahasa besar multimodal yang jelas menunjukkan fakta bahwa Apple sangat serius dalam mengembangkan AI. Saya belum berkesempatan untuk mencobanya.

• DBRX oleh Databricks (27 Maret 2024): Model terbuka yang memperkenalkan arsitektur campuran pakar berbutir halus (MoE), mencapai kinerja yang mengesankan dengan lebih sedikit parameter daripada GPT. Ini bisa sangat menarik bagi perusahaan enterprise, karena memberi mereka kemampuan untuk menjalankan model AI yang kuat di infrastruktur mereka sendiri. Fokus Databricks pada kebutuhan perusahaan seperti kepatuhan data dan kemampuan untuk menyesuaikan model untuk kasus penggunaan tertentu menjadikan DBRX pilihan menarik bagi banyak bisnis.

• Llama 3 oleh Meta (18 April 2024): Model terbuka terbaru Meta, dilatih pada kumpulan data yang sangat besar dan menawarkan kinerja sebanding dengan GPT dari hanya 1,5 tahun yang lalu. Saya sangat, sangat terkesan dengan kualitas output, bagaimana ia bereaksi terhadap prompt khusus, dan betapa serbaguna dan bermanfaatnya model ini. Tentu saja saya telah melihat LLama 2 sebelumnya tetapi tidak banyak menggunakannya. Facebook, WhatsApp, dan Instagram sekarang memiliki kemampuan yang didukung LLama 3 yang tertanam. Ketika Anda memikirkan betapa mendapatkan data segar untuk melatih model mereka adalah masalah besar bagi perusahaan AI saat ini, pertimbangkan berapa miliar pengguna yang dimiliki platform ini. Meta berada dalam posisi yang bagus. Pembelajaran penguatan dengan umpan balik manusia adalah kunci untuk membuat model AI lebih cerdas dan menciptakan generasi berikutnya.

• Phi-3 oleh Microsoft (23 April 2024): Keluarga model bahasa kecil (SLM) yang dirancang untuk efisiensi dan kinerja, sangat cocok untuk komputasi edge dan skenario offline. Saya menikmati set interaksi pertama saya dengan model Phi-3 dan saya percaya mereka akan menemukan ceruk yang kuat dalam aplikasi yang memprioritaskan kecepatan, privasi, dan kemampuan on-device daripada kekuatan mentah.

Garis waktu ini menunjukkan laju inovasi yang cepat dan keragaman lanskap model AI yang semakin meningkat hanya dalam beberapa bulan. Setiap rilis membawa kemampuan, arsitektur, dan potensi kasus penggunaan baru, memberikan pengembang dan bisnis banyak pilihan untuk dipilih.

## OpenAI dan Kebangkitan Arsitektur AI yang Lebih Efisien

Tapi di mana OpenAI dalam semua ini? Perusahaan yang menjalankan ChatGPT yang sangat terkenal dan masih mendominasi sebagian besar lanskap AI dengan model GPT-nya, absen secara mencolok dari gelombang rilis baru-baru ini (jika Anda mengabaikan pengumuman SORA untuk sementara). Sementara mereka mungkin sedang mengerjakan GPT-5 di belakang layar, jelas bahwa beberapa arsitektur yang lebih baru, khususnya yang menggunakan teknik campuran pakar (MoE), mulai menantang supremasi GPT.

Model seperti DBRX dan Llama 3 telah menunjukkan bahwa mungkin untuk mencapai kinerja yang mengesankan dengan lebih sedikit parameter dan arsitektur yang lebih efisien. Dan pergeseran menuju model MoE, yang dapat memberikan hasil yang lebih baik dengan persyaratan infrastruktur yang lebih kecil, secara efektif memakan makan siang OpenAI dengan mengikis keunggulan kompetitif yang pernah dimiliki GPT.

Jadi, bagaimana kita menavigasi era baru pilihan dan aksesibilitas model AI ini untuk menemukan yang paling sesuai dengan kebutuhan kita?

## Memanfaatkan Keragaman Model AI

Saat kita menavigasi era baru pilihan dan aksesibilitas model AI ini, penting untuk mengenali bahwa tidak ada solusi satu ukuran untuk semua. Sama seperti otak kita menggunakan sistem yang berbeda untuk berbagai tugas, mulai dari yang otomatis dan tidak sadar (seperti mengikat sepatu) hingga yang disengaja dan analitis (seperti memecahkan masalah matematika yang kompleks), kita dapat memanfaatkan model AI yang berbeda untuk tujuan tertentu.

Dalam bukunya "Thinking, Fast and Slow," psikolog Daniel Kahneman memperkenalkan konsep dua sistem yang berbeda dalam pikiran kita: Sistem 1, yang beroperasi secara otomatis dan cepat, dan Sistem 2, yang mengalokasikan perhatian pada aktivitas mental yang lebih melelahkan. Kita dapat menerapkan kerangka kerja ini pada dunia model AI, menggunakan model yang lebih kecil dan lebih efisien untuk tugas-tugas yang membutuhkan respons cepat dan sumber daya komputasi minimal (mirip dengan Sistem 1) dan model yang lebih besar dan lebih kompleks untuk tugas-tugas yang menuntut penalaran dan analisis yang lebih mendalam (mirip dengan Sistem 2).

Selain itu, kita dapat menggabungkan model yang unggul dalam tugas-tugas spesifik untuk menciptakan sistem AI yang kuat dan beragam. Misalnya, kita mungkin menggunakan model seperti Phi-3 untuk komputasi edge dan skenario offline, Gemma untuk pemrosesan on-device yang ringan, dan DBRX atau Llama 3 untuk tugas-tugas berbasis cloud yang lebih kompleks. Dengan memahami kekuatan dan kelemahan setiap model dan menggabungkannya secara strategis, kita dapat membangun aplikasi AI yang lebih efisien, efektif, dan mudah beradaptasi dengan berbagai kasus penggunaan.

## Anda Dapat Menggunakan Pendekatan yang Fleksibel dan Terinformasi

Pada akhirnya, kunci keberhasilan dalam lanskap baru ini adalah mendekati pemilihan dan penerapan model AI dengan pola pikir yang fleksibel dan terinformasi. Dengan tetap mengikuti perkembangan terbaru, bereksperimen dengan berbagai model, dan mempertimbangkan dengan cermat kebutuhan dan kendala spesifik setiap proyek, pengembang dan bisnis dapat memanfaatkan kekuatan era AI baru ini sambil menghindari jebakan ketergantungan berlebihan pada satu model atau penyedia mana pun.

Ini adalah waktu yang menarik untuk AI, dan saat kita melangkah maju, mari kita merangkul keragaman dan aksesibilitas lanskap model AI, karena ini jelas merupakan langkah signifikan dalam demokratisasi dan kemajuan kecerdasan buatan.