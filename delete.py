def hapus_tiket(daftar_tiket):
    """
    Fungsi untuk menghapus tiket dari sistem.
    Hanya tiket berstatus 'Selesai' yang dapat dihapus.
    """
    print("\n--- FITUR HAPUS TIKET ---")
    # Input 1: Kode tiket yang akan dihapus
    kode_cari = input("Masukkan kode tiket yang akan dihapus: ")
    
    # Validasi 1: Mencari tiket berdasarkan kode
    tiket_target = None
    for tiket in daftar_tiket:
        # Mengacu pada penamaan atribut di dokumen (kode_tiket)
        if tiket["kode_tiket"] == kode_cari:
            tiket_target = tiket
            break
            
    # Output (tidak ditemukan)
    if tiket_target is None:
        print(f"Tiket dengan kode '{kode_cari}' tidak ditemukan.")
        return

    # Validasi 2: Pengecekan status sebelum menampilkan konfirmasi
    if tiket_target["status"] != "Selesai":
        # Output (belum selesai)
        print(f"Tiket {kode_cari} tidak dapat dihapus karena masih berstatus {tiket_target['status']}. Selesaikan penanganan tiket terlebih dahulu sebelum menghapusnya.")
        return

    # Menampilkan detail tiket sebelum meminta konfirmasi
    print("\nDetail Tiket yang akan dihapus:")
    print(f"Kode          : {tiket_target['kode_tiket']}")
    print(f"Nama Pelapor  : {tiket_target['nama_pelapor']}")
    print(f"Jenis Masalah : {tiket_target['jenis_masalah']}")
    print(f"Prioritas     : {tiket_target['prioritas']}")
    print(f"Status        : {tiket_target['status']}")
    
    # Input 2 & Validasi 3: Konfirmasi penghapusan (y/n)
    konfirmasi = input("\nApakah Anda yakin ingin menghapus tiket ini? (y/n): ").strip().lower()
    
    if konfirmasi == 'y':
        # Menghapus tiket dari list (Array of Struct)
        daftar_tiket.remove(tiket_target)
        # Output (sukses)
        print(f"Tiket {kode_cari} dari {tiket_target['nama_pelapor']} berhasil dihapus dari sistem.")
    else:
        # Output (batal)
        print("Penghapusan dibatalkan.")

# ==========================================
# CONTOH CARA PENGGUNAAN (TESTING):
# ==========================================
if __name__ == "__main__":
    # Contoh data dummy (Array of Struct / List of Dict)
    data_tiket_dummy = [
        {
            "kode_tiket": "TKT001",
            "nama_pelapor": "Andi Wijaya",
            "jenis_masalah": "Hardware",
            "deskripsi": "Laptop tidak bisa menyala",
            "prioritas": "Sedang",
            "status": "Selesai" # Bisa dihapus
        },
        {
            "kode_tiket": "TKT002",
            "nama_pelapor": "Budi Santoso",
            "jenis_masalah": "Jaringan",
            "deskripsi": "Internet putus",
            "prioritas": "Tinggi",
            "status": "Diproses" # Tidak bisa dihapus
        }
    ]

    # Uji coba hapus tiket yang belum selesai
    hapus_tiket(data_tiket_dummy)
    
    # Uji coba hapus tiket yang sudah selesai
    hapus_tiket(data_tiket_dummy)