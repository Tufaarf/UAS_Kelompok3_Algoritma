# Sistem Helpdesk / Tiket Layanan (CLI)
> **Tugas Besar / UTS Kelompok 3 — Algoritma dan Pemrograman**  
> Implementasi Struktur Data *Array of Struct* (List of Dictionary) menggunakan 100% Native Python tanpa library eksternal.

---

## 1. Nama & Anggota Kelompok

**Nama Sistem:** Sistem Helpdesk / Tiket Layanan (CLI)  
**Kelompok:** Kelompok 3  

| No | Nama Anggota | NIM | Fokus / Peran |
|:--:|:-------------|:---:|:--------------|
| 1  | **Daffa Thufail Arrofi** | 25083000022 | Project manager, quality assurance, develop fitur Tambah Tiket & Update Status |
| 2  | **Astridia Veronic Zonna Basuki** | 25083000040 | Tampilkan Semua Tiket |
| 3  | **Daniela Yuanita Salsabila** | 25083000045 | Cari Tiket |
| 4  | **Yohanes Raditya Jati Prasetya** | 25083000014 | Filter Tiket |
| 5  | **I Ketut Gede Wicaksana** | 25083000010 | Hapus Tiket |

---

## 2. Deskripsi Sistem

Sistem Helpdesk / Tiket Layanan adalah aplikasi berbasis Command Line Interface (CLI) menggunakan Python murni yang dirancang untuk mengelola pelaporan keluhan dan permintaan penanganan masalah teknis secara terpusat. Sistem ini memanfaatkan struktur data *Array of Struct* (List of Dictionary) dalam memori untuk mencatat, memperbarui, mencari, memfilter, serta menghapus data tiket layanan secara terstruktur dan efisien. Selain itu, program ini memfasilitasi dua peran pengguna, yaitu *User/Pelapor* untuk mengajukan dan memantau status tiket secara mandiri, serta *Admin/Staf Helpdesk* untuk memproses tanggapan dan mengelola siklus hidup tiket dari awal hingga selesai.

---

## 3. Cara Menjalankan

Program ini dibangun menggunakan **100% Native Python**, sehingga tidak memerlukan instalasi dependensi atau paket eksternal tambahan (`pip`). 

Ikuti langkah-langkah berikut untuk menjalankan program dari awal:

1. **Clone Repository**
   Buka terminal atau command prompt, lalu unduh repository ini:
   ```bash
   git clone https://github.com/Tufaarf/UTS_Kelompok3_Algoritma.git
   ```

2. **Masuk ke Direktori Proyek**
   ```bash
   cd UTS_Kelompok3_Algoritma
   ```

3. **Pastikan Python Terinstal**
   Pastikan Python versi 3.x telah terpasang di perangkat Anda:
   ```bash
   python --version
   ```

4. **Jalankan Program Utama**
   Eksekusi file utama (`main.py`):
   ```bash
   python main.py
   ```

---

## 4. Fitur yang Sudah Ada

Berikut adalah daftar fitur utama dan fitur pendukung yang telah diimplementasikan dalam versi ini:

### Fitur Utama (F1 - F6)

1. **F1: Tambah Tiket Baru (`function/add.py`)**
   - Menambahkan laporan tiket baru ke dalam sistem (*Array of Struct*).
   - Validasi kode tiket unik (*case-insensitive*) untuk mencegah duplikasi kode tiket.
   - Validasi pilihan kategori jenis masalah: `Hardware`, `Software`, `Jaringan`, atau `Lainnya`.
   - Validasi pilihan tingkat prioritas: `Rendah`, `Sedang`, atau `Tinggi`.
   - Status tiket otomatis diinisialisasi ke status awal `"Menunggu"`.

2. **F2: Tampilkan Semua Tiket (`function/tiket.py`)**
   - Menampilkan seluruh daftar tiket yang tersimpan dalam format tabel terminal yang rapi dan terstruktur.
   - Kolom menampilkan: No, Kode Tiket, Nama Pelapor, Jenis Masalah, Prioritas, dan Status.
   - Dilengkapi ringkasan rekapitulasi data di bagian bawah tabel (Total Tiket, Jumlah Menunggu, Diproses, dan Selesai).

3. **F3: Cari Tiket (`function/search.py`)**
   - Pencarian berdasarkan **Kode Tiket**: Pencarian eksak (*exact match*) yang menampilkan detail lengkap tiket beserta respon/tanggapan dari admin.
   - Pencarian berdasarkan **Nama Pelapor**: Pencarian berbasis kata kunci (*partial match*) dan tidak sensitif huruf besar/kecil (*case-insensitive*) yang ditampilkan dalam bentuk tabel ringkas.

4. **F4: Update Status Tiket (`function/update.py`)**
   - Pembaruan status tiket dengan alur penanganan satu arah yang terstandarisasi:  
     $$\text{Menunggu} \longrightarrow \text{Diproses} \longrightarrow \text{Selesai}$$
   - Tiket yang telah berstatus `"Selesai"` tidak dapat diperbarui lagi.
   - Dilengkapi konfirmasi interaktif (`y/n`) sebelum perubahan status disimpan.
   - Fitur pemberian tanggapan/solusi teknis oleh staf helpdesk.

5. **F5: Filter Tiket Berdasarkan Jenis Masalah (`function/filter.py`)**
   - Menyaring dan menampilkan daftar tiket berdasarkan kategori masalah (`Hardware`, `Software`, `Jaringan`, atau `Lainnya`).
   - Memudahkan staf dan teknisi untuk meninjau tiket sesuai dengan bidang spesialisasi penanganan.

6. **F6: Hapus Tiket (`function/delete.py`)**
   - Menghapus tiket dari sistem berdasarkan kode tiket.
   - Validasi aturan integritas: hanya tiket dengan status `"Selesai"` yang diizinkan untuk dihapus dari sistem.
   - Konfirmasi persetujuan (`y/n`) sebelum tiket dihapus secara permanen dari memori.

### Fitur Tambahan & Utilitas
- **Dukungan Multi-Peran (`index.py`)**: Portal khusus *User* (pelapor tiket) dan Panel khusus *Admin / Staf Helpdesk*.
- **Manajemen Tiket Mandiri untuk User**: Pelapor dapat melihat daftar tiket miliknya sendiri, mengecek balasan teknisi, serta membatalkan tiket miliknya.
- **Utilitas Terminal (`function/utils.py`)**: Fungsi pembersihan layar terminal (*cross-platform*) dan jeda baca untuk kenyamanan antarmuka pengguna.

---

## 5. Pembagian Tugas

Rincian pembagian tugas pengerjaan modul dan fitur dalam kelompok:

| Anggota Kelompok | Tugas & Modul yang Dikerjakan | Rincian Tanggung Jawab |
|:---|:---|:---|
| **Daffa Thufail Arrofi (Tufa)** | **Project Manager**,<br>**Quality Assurance (QA)**,<br>**F1: Tambah Tiket Baru** &<br>**F4: Update Status Tiket** | • **Project Manager**: Mengoordinasikan pembagian tugas tim, menyusun struktur direktori/arsitektur proyek, serta mengintegrasikan seluruh modul fungsi ke dalam sistem utama (`index.py` & `main.py`).<br>• **Quality Assurance**: Melakukan pengujian fungsionalitas sistem (*testing*), memvalidasi alur program dan penanganan error, serta memastikan kode berjalan stabil dan bersih.<br>• **F1 & F4**: Mengimplementasikan fungsi penambahan tiket baru (`tambah_tiket`) dengan validasi kode tiket anti-duplikat, kategori masalah, prioritas, serta alur pembaruan status tiket satu arah (`Menunggu` $\rightarrow$ `Diproses` $\rightarrow$ `Selesai`) disertai dialog konfirmasi. |
| **Astridia Veronic Zonna Basuki (Astrid)** | **F2: Tampilkan Semua Tiket** | • Mengimplementasikan fungsi penampil seluruh tiket (`lihat_daftar_tiket`) dalam format tabel terformat.<br>• Membuat rekapitulasi ringkasan statistik total tiket dan perhitungan jumlah per status tiket. |
| **Daniela Yuanita Salsabila (Aleya)** | **F3: Cari Tiket** | • Mengimplementasikan fungsi pencarian tiket (`menu_cari_tiket`).<br>• Menyediakan mode pencarian *exact match* untuk kode tiket (menampilkan rincian lengkap) dan *partial/case-insensitive match* untuk pencarian berdasarkan nama pelapor. |
| **Yohanes Raditya Jati Prasetya (Radit)** | **F5: Filter Tiket Berdasarkan Jenis Masalah** | • Mengimplementasikan fitur filter tiket (`filter_tiket`) berdasarkan kategori jenis masalah (`Hardware`, `Software`, `Jaringan`, `Lainnya`).<br>• Menampilkan hasil penyaringan dalam format tabel. |
| **I Ketut Gede Wicaksana (Wicak)** | **F6: Hapus Tiket** | • Mengimplementasikan fungsi penghapusan tiket (`hapus_tiket`) dari memori sistem.<br>• Menerapkan validasi keamanan status (hanya tiket dengan status `"Selesai"` yang boleh dihapus) disertai konfirmasi (`y/n`). |