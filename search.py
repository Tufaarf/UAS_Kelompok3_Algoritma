"""
test
cari_tiket.py
Fitur 3 (F3): Cari Tiket
Penanggung jawab: Aleya

Mencari tiket berdasarkan:
  1. Kode tiket        -> exact match (harus persis sama), hasil maksimal 1 tiket
  2. Nama pelapor      -> partial match, tidak case sensitive, bisa lebih dari 1 hasil

Data tiket berupa list of dict (Array of Struct), contoh satu tiket:
    {
        "kode_tiket": "TKT001",
        "nama_pelapor": "Andi Wijaya",
        "jenis_masalah": "Hardware",
        "deskripsi": "Laptop tidak bisa menyala",
        "prioritas": "Sedang",
        "status": "Menunggu",
    }
"""


# ---------------------------------------------------------------------------
# FUNGSI PENCARIAN (logika murni, tidak ada print/input supaya mudah diuji)
# ---------------------------------------------------------------------------

def cari_berdasarkan_kode(daftar_tiket, kode):
    """Cari 1 tiket dengan kode yang PERSIS sama.

    Mengembalikan dict tiket jika ditemukan, atau None jika tidak ada.
    """
    for tiket in daftar_tiket:
        if tiket["kode_tiket"] == kode:  # exact match
            return tiket
    return None


def cari_berdasarkan_nama(daftar_tiket, kata_kunci):
    """Cari semua tiket yang nama pelapornya MENGANDUNG kata kunci.

    Tidak case sensitive: keduanya diubah ke huruf kecil sebelum dibandingkan.
    Mengembalikan list tiket yang cocok (bisa kosong).
    """
    kata_kunci = kata_kunci.lower()
    hasil = []
    for tiket in daftar_tiket:
        if kata_kunci in tiket["nama_pelapor"].lower():  # partial match
            hasil.append(tiket)
    return hasil


# ---------------------------------------------------------------------------
# FUNGSI TAMPILAN
# ---------------------------------------------------------------------------

def tampilkan_detail_tiket(tiket):
    """Tampilkan seluruh atribut satu tiket (termasuk deskripsi)."""
    print("\n=== DETAIL TIKET ===")
    print(f"Kode Tiket    : {tiket['kode_tiket']}")
    print(f"Nama Pelapor  : {tiket['nama_pelapor']}")
    print(f"Jenis Masalah : {tiket['jenis_masalah']}")
    print(f"Deskripsi     : {tiket['deskripsi']}")
    print(f"Prioritas     : [{tiket['prioritas'].upper()}]")
    print(f"Status        : [{tiket['status'].upper()}]")


def tampilkan_tabel_tiket(daftar_hasil):
    """Tampilkan tiket dalam bentuk tabel (kolom sama seperti Fitur 2).

    Kolom: No, Kode, Nama Pelapor, Jenis Masalah, Prioritas, Status.
    Deskripsi sengaja tidak ditampilkan di tabel.
    """
    garis = "-" * 85
    print(garis)
    print(f"{'No':<4}{'Kode':<12}{'Nama Pelapor':<24}{'Jenis Masalah':<16}"
          f"{'Prioritas':<12}{'Status':<12}")
    print(garis)
    for nomor, tiket in enumerate(daftar_hasil, start=1):
        prioritas = f"[{tiket['prioritas'].upper()}]"
        status = f"[{tiket['status'].upper()}]"
        print(f"{nomor:<4}{tiket['kode_tiket']:<12}{tiket['nama_pelapor']:<24}"
              f"{tiket['jenis_masalah']:<16}{prioritas:<12}{status:<12}")
    print(garis)


# ---------------------------------------------------------------------------
# FUNGSI MENU (interaksi dengan staf) -> dipanggil dari main.py
# ---------------------------------------------------------------------------

def menu_cari_tiket(daftar_tiket):
    """Alur Fitur 3: pilih mode pencarian, input kata kunci, tampilkan hasil."""
    print("\n=== CARI TIKET ===")
    print("1. Cari berdasarkan kode tiket")
    print("2. Cari berdasarkan nama pelapor")
    mode = input("Pilih mode pencarian (1/2): ").strip()

    # Validasi pilihan mode
    if mode not in ("1", "2"):
        print("Pilihan tidak valid. Masukkan 1 atau 2.")
        return

    # Validasi: kata kunci tidak boleh kosong
    kata_kunci = input("Masukkan kata kunci: ").strip()
    if kata_kunci == "":
        print("Kata kunci tidak boleh kosong.")
        return

    if mode == "1":
        # --- Pencarian by kode (exact match, 1 hasil) ---
        tiket = cari_berdasarkan_kode(daftar_tiket, kata_kunci)
        if tiket is None:
            print(f"Tiket dengan kode '{kata_kunci}' tidak ditemukan.")
        else:
            print("Jumlah hasil ditemukan:1")
            tampilkan_detail_tiket(tiket)
    else:
        # --- Pencarian by nama pelapor (partial match, bisa banyak hasil) ---
        hasil = cari_berdasarkan_nama(daftar_tiket, kata_kunci)
        if len(hasil) == 0:
            print(f"Tiket dengan nama pelapor '{kata_kunci}' tidak ditemukan.")
        else:
            print(f"\nDitemukan {len(hasil)} tiket dengan nama pelapor "
                  f"mengandung '{kata_kunci}':")
            tampilkan_tabel_tiket(hasil)


# ---------------------------------------------------------------------------
# UJI MANDIRI: jalankan `python cari_tiket.py` untuk mencoba F3 sendirian
# (bagian ini tidak ikut jalan saat file di-import oleh main.py)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    data_contoh = [
        {"kode_tiket": "TKT001", "nama_pelapor": "Andi Wijaya",
         "jenis_masalah": "Hardware", "deskripsi": "Laptop tidak bisa menyala",
         "prioritas": "Sedang", "status": "Menunggu"},
        {"kode_tiket": "TKT002", "nama_pelapor": "Andi Saputra",
         "jenis_masalah": "Jaringan", "deskripsi": "Wifi sering putus",
         "prioritas": "Tinggi", "status": "Diproses"},
        {"kode_tiket": "TKT003", "nama_pelapor": "Budi Santoso",
         "jenis_masalah": "Software", "deskripsi": "Aplikasi tidak bisa dibuka",
         "prioritas": "Rendah", "status": "Selesai"},
    ]

    while True:
        menu_cari_tiket(data_contoh)
        ulang = input("\nCari lagi? (y/n): ").strip().lower()
        if ulang != "y":
            break