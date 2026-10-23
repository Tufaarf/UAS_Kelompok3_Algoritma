"""
Fitur 1: Tambah Tiket Baru (Native Python)
Deskripsi: Staf / Pengguna dapat mencatat tiket laporan masalah baru ke dalam sistem.
"""

JENIS_MASALAH_VALID = {
    "hardware": "Hardware",
    "software": "Software",
    "jaringan": "Jaringan",
    "lainnya": "Lainnya"
}

PRIORITAS_VALID = {
    "rendah": "Rendah",
    "sedang": "Sedang",
    "tinggi": "Tinggi"
}


def tambah_tiket(daftar_tiket, nama_pelapor_default=None):
    """
    Menambahkan tiket baru ke dalam daftar_tiket (Array of Struct / List of Dict).
    Mendukung pengisian otomatis nama_pelapor jika dipanggil dari portal User.
    Menggunakan 100% native Python tanpa library eksternal.
    """
    print("\n--- FITUR: TAMBAH TIKET BARU ---")

    # 1. Input dan Validasi: kode_tiket
    kode_input = input("Masukkan Kode Tiket (misal: TKT001): ").strip()
    if not kode_input:
        print("[Error] Kode tiket tidak boleh kosong.")
        return False

    # Validasi duplikasi kode tiket (case-insensitive)
    for tiket in daftar_tiket:
        if tiket["kode_tiket"].strip().lower() == kode_input.lower():
            print(f"[Error] Kode tiket '{kode_input}' sudah ada dalam sistem. Kode tidak boleh duplikat.")
            return False

    # 2. Input dan Validasi: nama_pelapor
    if nama_pelapor_default:
        nama_input = nama_pelapor_default.strip()
        print(f"Nama Pelapor  : {nama_input}")
    else:
        nama_input = input("Masukkan Nama Pelapor: ").strip()
        if not nama_input:
            print("[Error] Nama pelapor tidak boleh kosong.")
            return False

    # 3. Input dan Validasi: jenis_masalah
    print("Pilihan Jenis Masalah: Hardware, Software, Jaringan, Lainnya")
    jenis_input = input("Masukkan Jenis Masalah: ").strip()
    if jenis_input.lower() not in JENIS_MASALAH_VALID:
        print("[Error] Jenis masalah tidak valid! Hanya boleh: Hardware, Software, Jaringan, Lainnya.")
        return False
    jenis_masalah = JENIS_MASALAH_VALID[jenis_input.lower()]

    # 4. Input dan Validasi: deskripsi
    deskripsi_input = input("Masukkan Deskripsi Masalah: ").strip()
    if not deskripsi_input:
        print("[Error] Deskripsi tidak boleh kosong.")
        return False

    # 5. Input dan Validasi: prioritas
    print("Pilihan Prioritas: Rendah, Sedang, Tinggi")
    prioritas_input = input("Masukkan Prioritas: ").strip()
    if prioritas_input.lower() not in PRIORITAS_VALID:
        print("[Error] Prioritas tidak valid! Hanya boleh: Rendah, Sedang, Tinggi.")
        return False
    prioritas = PRIORITAS_VALID[prioritas_input.lower()]

    # 6. Status otomatis "Menunggu"
    status = "Menunggu"

    # Menyimpan tiket sebagai Dictionary (Struct)
    # Mempertahankan 6 atribut wajib + atribut opsional tanggapan untuk alur admin
    tiket_baru = {
        "kode_tiket": kode_input,
        "nama_pelapor": nama_input,
        "jenis_masalah": jenis_masalah,
        "deskripsi": deskripsi_input,
        "prioritas": prioritas,
        "status": status,
        "tanggapan": "-"
    }

    # Menambahkan ke list tiket (Array of Struct)
    daftar_tiket.append(tiket_baru)

    # Output konfirmasi sukses
    print(f"\nTiket {kode_input} dari {nama_input} berhasil dicatat.")
    return True
