"""
Fitur 3: Cari Tiket & Lihat Detail (Native Python)
Deskripsi: Staf / Pengguna dapat mencari tiket dan melihat detail lengkap tiket.
"""

def cari_berdasarkan_kode(daftar_tiket, kode):
    """
    Cari 1 tiket dengan kode yang PERSIS sama (exact match).
    Mengembalikan dict tiket jika ditemukan, atau None jika tidak ada.
    """
    for tiket in daftar_tiket:
        if tiket["kode_tiket"].strip().lower() == kode.strip().lower():
            return tiket
    return None


def cari_berdasarkan_nama(daftar_tiket, kata_kunci):
    """
    Cari semua tiket yang nama pelapornya MENGANDUNG kata kunci (partial match).
    Tidak case-sensitive. Mengembalikan list tiket yang cocok.
    """
    kata_kunci = kata_kunci.lower()
    hasil = []
    for tiket in daftar_tiket:
        if kata_kunci in tiket["nama_pelapor"].lower():
            hasil.append(tiket)
    return hasil


def tampilkan_detail_tiket(tiket):
    """Tampilkan seluruh atribut satu tiket (termasuk deskripsi & respon admin)."""
    print("\n=== DETAIL TIKET ===")
    print(f"Kode Tiket       : {tiket['kode_tiket']}")
    print(f"Nama Pelapor     : {tiket['nama_pelapor']}")
    print(f"Jenis Masalah    : {tiket['jenis_masalah']}")
    print(f"Deskripsi        : {tiket['deskripsi']}")
    print(f"Prioritas        : [{tiket['prioritas'].upper()}]")
    print(f"Status           : [{tiket['status'].upper()}]")
    tanggapan = tiket.get("tanggapan", "-")
    print(f"Tanggapan Admin  : {tanggapan}")


def tampilkan_tabel_tiket(daftar_hasil):
    """
    Tampilkan tiket dalam bentuk tabel (kolom sama seperti Fitur 2).
    """
    w_no, w_kode, w_nama, w_jenis, w_prio, w_status = 4, 10, 22, 18, 12, 14
    garis = "-" * (w_no + w_kode + w_nama + w_jenis + w_prio + w_status + (5 * 3))

    print(garis)
    print(
        f"{'No':<{w_no}} | {'Kode':<{w_kode}} | {'Nama Pelapor':<{w_nama}} | "
        f"{'Jenis Masalah':<{w_jenis}} | {'Prioritas':<{w_prio}} | {'Status':<{w_status}}"
    )
    print(garis)
    for nomor, tiket in enumerate(daftar_hasil, start=1):
        nama = tiket["nama_pelapor"]
        nama_fmt = (nama[:19] + "...") if len(nama) > w_nama else nama
        jenis = tiket["jenis_masalah"]
        jenis_fmt = (jenis[:15] + "...") if len(jenis) > w_jenis else jenis
        prioritas = f"[{tiket['prioritas'].upper()}]"
        status = f"[{tiket['status'].upper()}]"

        print(
            f"{nomor:<{w_no}} | {tiket['kode_tiket']:<{w_kode}} | {nama_fmt:<{w_nama}} | "
            f"{jenis_fmt:<{w_jenis}} | {prioritas:<{w_prio}} | {status:<{w_status}}"
        )
    print(garis)


def menu_cari_tiket(daftar_tiket):
    """Alur Fitur 3 untuk Admin: pilih mode pencarian, input kata kunci, tampilkan hasil."""
    print("\n--- FITUR 3: CARI TIKET (ADMIN) ---")
    print("1. Cari berdasarkan kode tiket")
    print("2. Cari berdasarkan nama pelapor")
    mode = input("Pilih mode pencarian (1/2): ").strip()

    if mode not in ("1", "2"):
        print("[Error] Pilihan tidak valid. Masukkan 1 atau 2.")
        return

    kata_kunci = input("Masukkan kata kunci: ").strip()
    if not kata_kunci:
        print("[Error] Kata kunci tidak boleh kosong.")
        return

    if mode == "1":
        tiket = cari_berdasarkan_kode(daftar_tiket, kata_kunci)
        if tiket is None:
            print(f"Tiket dengan kode '{kata_kunci}' tidak ditemukan.")
        else:
            print(f"\nJumlah hasil ditemukan: 1")
            tampilkan_detail_tiket(tiket)
    else:
        hasil = cari_berdasarkan_nama(daftar_tiket, kata_kunci)
        if len(hasil) == 0:
            print(f"Tiket dengan nama pelapor '{kata_kunci}' tidak ditemukan.")
        else:
            print(f"\nJumlah hasil ditemukan: {len(hasil)} (nama pelapor mengandung '{kata_kunci}')")
            tampilkan_tabel_tiket(hasil)


def cari_tiket_user(daftar_tiket, nama_user):
    """
    Mencari dan menampilkan detail tiket milik user tertentu.
    User hanya dapat melihat tiket miliknya sendiri.
    """
    print("\n--- LIHAT DETAIL & TANGGAPAN TIKET SAYA ---")
    kode_input = input("Masukkan kode tiket Anda: ").strip()
    if not kode_input:
        print("[Error] Kode tiket tidak boleh kosong.")
        return

    tiket = cari_berdasarkan_kode(daftar_tiket, kode_input)
    if tiket is None:
        print(f"Tiket dengan kode '{kode_input}' tidak ditemukan.")
        return

    # Validasi kepemilikan tiket
    if tiket["nama_pelapor"].strip().lower() != nama_user.strip().lower():
        print(f"[Akses Ditolak] Tiket '{kode_input}' bukan milik Anda.")
        return

    tampilkan_detail_tiket(tiket)
