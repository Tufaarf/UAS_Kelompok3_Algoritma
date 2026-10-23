"""
Fitur 6: Hapus & Batalkan Tiket (Native Python)
Deskripsi: Menghapus tiket dari sistem sesuai hak akses Admin atau Pengguna (User).
"""

def hapus_tiket(daftar_tiket):
    """
    Fungsi untuk menghapus tiket dari sistem oleh Admin.
    Hanya tiket berstatus 'Selesai' yang dapat dihapus, dengan konfirmasi y/n.
    """
    print("\n--- FITUR 6: HAPUS TIKET (ADMIN) ---")

    kode_cari = input("Masukkan kode tiket yang akan dihapus: ").strip()
    if not kode_cari:
        print("[Error] Kode tiket tidak boleh kosong.")
        return

    # Mencari tiket berdasarkan kode_tiket
    tiket_target = None
    for tiket in daftar_tiket:
        if tiket["kode_tiket"].strip().lower() == kode_cari.lower():
            tiket_target = tiket
            break

    if tiket_target is None:
        print(f"Tiket dengan kode '{kode_cari}' tidak ditemukan.")
        return

    # Validasi status sebelum menampilkan konfirmasi: Hanya status "Selesai" yang boleh dihapus
    if tiket_target["status"] != "Selesai":
        print(f"Tiket {tiket_target['kode_tiket']} tidak dapat dihapus karena masih berstatus {tiket_target['status']}. Selesaikan penanganan tiket terlebih dahulu sebelum menghapusnya.")
        return

    # Detail tiket sebelum konfirmasi
    print("\nDetail Tiket yang akan dihapus:")
    print(f"Kode Tiket    : {tiket_target['kode_tiket']}")
    print(f"Nama Pelapor  : {tiket_target['nama_pelapor']}")
    print(f"Jenis Masalah : {tiket_target['jenis_masalah']}")
    print(f"Prioritas     : {tiket_target['prioritas']}")
    print(f"Status        : {tiket_target['status']}")

    konfirmasi = input("\nApakah Anda yakin ingin menghapus tiket ini? (y/n): ").strip().lower()

    if konfirmasi == "y":
        daftar_tiket.remove(tiket_target)
        print(f"Tiket {tiket_target['kode_tiket']} dari {tiket_target['nama_pelapor']} berhasil dihapus dari sistem.")
    else:
        print("Penghapusan dibatalkan.")


def batalkan_tiket_user(daftar_tiket, nama_user):
    """
    Fungsi untuk User: Membatalkan atau menghapus tiket miliknya sendiri.
    User hanya dapat mengelola tiket dengan nama_pelapor yang sesuai identitasnya.
    """
    print(f"\n--- BATALKAN / HAPUS TIKET SAYA ({nama_user}) ---")

    kode_cari = input("Masukkan kode tiket yang ingin dibatalkan/dihapus: ").strip()
    if not kode_cari:
        print("[Error] Kode tiket tidak boleh kosong.")
        return

    tiket_target = None
    for tiket in daftar_tiket:
        if tiket["kode_tiket"].strip().lower() == kode_cari.lower():
            tiket_target = tiket
            break

    if tiket_target is None:
        print(f"Tiket dengan kode '{kode_cari}' tidak ditemukan.")
        return

    # Validasi kepemilikan tiket
    if tiket_target["nama_pelapor"].strip().lower() != nama_user.strip().lower():
        print(f"[Akses Ditolak] Tiket '{kode_cari}' bukan milik Anda. Anda hanya dapat mengelola tiket Anda sendiri.")
        return

    print("\nDetail Tiket Anda:")
    print(f"Kode Tiket    : {tiket_target['kode_tiket']}")
    print(f"Jenis Masalah : {tiket_target['jenis_masalah']}")
    print(f"Deskripsi     : {tiket_target['deskripsi']}")
    print(f"Status        : {tiket_target['status']}")

    if tiket_target["status"] == "Diproses":
        print("\n[Perhatian] Tiket ini sedang diproses oleh staf/teknisi.")

    konfirmasi = input("\nApakah Anda yakin ingin membatalkan/menghapus tiket ini? (y/n): ").strip().lower()

    if konfirmasi == "y":
        daftar_tiket.remove(tiket_target)
        print(f"Tiket {tiket_target['kode_tiket']} berhasil dibatalkan dan dihapus.")
    else:
        print("Pembatalan tiket dibatalkan.")
