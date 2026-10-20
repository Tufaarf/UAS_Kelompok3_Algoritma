"""
Fitur: Lihat Daftar Tiket (Staf)
Staf dapat melihat seluruh daftar tiket yang tersimpan dalam sistem.
"""

# ------------------------------------------------------------
# Data tiket (contoh). Di sistem sebenarnya, data ini berasal
# dari penyimpanan (list/file/database). Kosongkan list ini
# untuk menguji tampilan "tidak ada tiket".
# ------------------------------------------------------------
daftar_tiket = [
    {
        "kode": "TKT-001",
        "nama_pelapor": "Budi Santoso",
        "jenis_masalah": "Jaringan",
        "prioritas": "TINGGI",
        "status": "MENUNGGU",
        "deskripsi": "Koneksi internet di ruang keuangan terputus sejak pagi.",
    },
    {
        "kode": "TKT-002",
        "nama_pelapor": "Siti Aminah",
        "jenis_masalah": "Printer",
        "prioritas": "SEDANG",
        "status": "DIPROSES",
        "deskripsi": "Printer lantai 2 tidak bisa mencetak.",
    },
    {
        "kode": "TKT-003",
        "nama_pelapor": "Andi Wijaya",
        "jenis_masalah": "Akun/Password",
        "prioritas": "RENDAH",
        "status": "SELESAI",
        "deskripsi": "Lupa password email kantor.",
    },
    {
        "kode": "TKT-004",
        "nama_pelapor": "Dewi Lestari",
        "jenis_masalah": "Perangkat Lunak",
        "prioritas": "TINGGI",
        "status": "DIPROSES",
        "deskripsi": "Aplikasi akuntansi sering crash saat membuka laporan.",
    },
]


def penanda(nilai):
    """Mengubah nilai menjadi penanda visual, misal 'TINGGI' -> '[TINGGI]'."""
    return f"[{nilai.upper()}]"


def lihat_daftar_tiket(tiket_list):
    """Menampilkan seluruh tiket dalam bentuk tabel beserta ringkasannya."""
    # Output (kosong)
    if not tiket_list:
        print("Belum ada tiket dalam sistem.")
        return

    # Lebar kolom
    w_no, w_kode, w_nama, w_jenis, w_prio, w_status = 4, 10, 22, 18, 10, 12
    garis = "-" * (w_no + w_kode + w_nama + w_jenis + w_prio + w_status + 5 * 3 + 4)

    print("\n" + "DAFTAR TIKET".center(len(garis)))
    print(garis)
    print(
        f"{'No':<{w_no}} | {'Kode':<{w_kode}} | {'Nama Pelapor':<{w_nama}} | "
        f"{'Jenis Masalah':<{w_jenis}} | {'Prioritas':<{w_prio}} | {'Status':<{w_status}}"
    )
    print(garis)

    # Output (ada data): kolom deskripsi sengaja tidak ditampilkan
    for i, t in enumerate(tiket_list, start=1):
        print(
            f"{i:<{w_no}} | {t['kode']:<{w_kode}} | {t['nama_pelapor']:<{w_nama}} | "
            f"{t['jenis_masalah']:<{w_jenis}} | {penanda(t['prioritas']):<{w_prio}} | "
            f"{penanda(t['status']):<{w_status}}"
        )
    print(garis)

    # Ringkasan di bawah tabel
    total = len(tiket_list)
    menunggu = sum(1 for t in tiket_list if t["status"].upper() == "MENUNGGU")
    diproses = sum(1 for t in tiket_list if t["status"].upper() == "DIPROSES")
    selesai = sum(1 for t in tiket_list if t["status"].upper() == "SELESAI")

    print(f"Total tiket : {total}")
    print(f"Menunggu    : {menunggu}")
    print(f"Diproses    : {diproses}")
    print(f"Selesai     : {selesai}")


def menu_staf():
    """Menu sederhana staf; fitur ini dipanggil tanpa input tambahan."""
    while True:
        print("\n=== MENU STAF ===")
        print("1. Lihat Daftar Tiket")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            lihat_daftar_tiket(daftar_tiket)
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    menu_staf()