"""
Fitur 4: Update Status & Menjawab Tiket (Native Python)
Deskripsi: Staf Admin dapat memajukan status penanganan tiket dan memberikan tanggapan/solusi.
"""

def update_status_tiket(daftar_tiket):
    """
    Memperbarui status penanganan tiket secara satu arah (Menunggu -> Diproses -> Selesai).
    Menampilkan informasi tiket dan meminta konfirmasi (y/n) sebelum mengubah status.
    """
    print("\n--- FITUR 4: UPDATE STATUS TIKET (ADMIN) ---")

    kode_input = input("Masukkan kode tiket yang akan diupdate: ").strip()
    if not kode_input:
        print("[Error] Kode tiket tidak boleh kosong.")
        return

    # Validasi 1: Mencari tiket berdasarkan kode_tiket
    tiket_target = None
    for tiket in daftar_tiket:
        if tiket["kode_tiket"].strip().lower() == kode_input.lower():
            tiket_target = tiket
            break

    if tiket_target is None:
        print(f"Tiket dengan kode '{kode_input}' tidak ditemukan.")
        return

    # Validasi 2 & 3: Cek status saat ini dan tentukan status berikutnya
    status_sekarang = tiket_target["status"]
    if status_sekarang == "Selesai":
        print(f"Tiket {tiket_target['kode_tiket']} sudah berstatus Selesai dan tidak dapat diperbarui lagi.")
        return
    elif status_sekarang == "Menunggu":
        status_berikutnya = "Diproses"
    elif status_sekarang == "Diproses":
        status_berikutnya = "Selesai"
    else:
        print(f"[Error] Status tiket '{status_sekarang}' tidak valid.")
        return

    # Validasi 4: Tampilkan informasi tiket dan konfirmasi
    print("\nInformasi Tiket:")
    print(f"Kode Tiket        : {tiket_target['kode_tiket']}")
    print(f"Nama Pelapor      : {tiket_target['nama_pelapor']}")
    print(f"Status Saat Ini   : {status_sekarang}")
    print(f"Status Berikutnya : {status_berikutnya}")

    konfirmasi = input("\nApakah Anda yakin ingin memperbarui status tiket ini? (y/n): ").strip().lower()

    if konfirmasi == "y":
        tiket_target["status"] = status_berikutnya
        print(f"Status tiket {tiket_target['kode_tiket']} berhasil diperbarui: {status_sekarang} menjadi {status_berikutnya}.")
    else:
        print("Pembaruan status dibatalkan.")


def jawab_tiket(daftar_tiket):
    """
    Fitur Admin: Memberikan respon, tanggapan, atau solusi atas laporan masalah tiket.
    Admin juga dapat memilih untuk memajukan status tiket secara bersamaan.
    """
    print("\n--- FITUR: JAWAB / BERI TANGGAPAN TIKET (ADMIN) ---")

    kode_input = input("Masukkan kode tiket yang akan dijawab: ").strip()
    if not kode_input:
        print("[Error] Kode tiket tidak boleh kosong.")
        return

    tiket_target = None
    for tiket in daftar_tiket:
        if tiket["kode_tiket"].strip().lower() == kode_input.lower():
            tiket_target = tiket
            break

    if tiket_target is None:
        print(f"Tiket dengan kode '{kode_input}' tidak ditemukan.")
        return

    print("\nInformasi Tiket:")
    print(f"Kode Tiket       : {tiket_target['kode_tiket']}")
    print(f"Nama Pelapor     : {tiket_target['nama_pelapor']}")
    print(f"Jenis Masalah    : {tiket_target['jenis_masalah']}")
    print(f"Deskripsi        : {tiket_target['deskripsi']}")
    print(f"Status Saat Ini  : {tiket_target['status']}")
    print(f"Tanggapan Lama   : {tiket_target.get('tanggapan', '-')}")

    tanggapan_baru = input("\nMasukkan Tanggapan / Solusi Admin: ").strip()
    if not tanggapan_baru:
        print("[Error] Tanggapan tidak boleh kosong.")
        return

    tiket_target["tanggapan"] = tanggapan_baru
    print(f"\nTanggapan untuk tiket {tiket_target['kode_tiket']} berhasil disimpan.")

    # Opsi sekaligus memperbarui status jika belum selesai
    status_sekarang = tiket_target["status"]
    if status_sekarang == "Menunggu":
        tanya = input("Status tiket masih 'Menunggu'. Ubah status menjadi 'Diproses'? (y/n): ").strip().lower()
        if tanya == "y":
            tiket_target["status"] = "Diproses"
            print(f"Status tiket {tiket_target['kode_tiket']} diperbarui menjadi Diproses.")
    elif status_sekarang == "Diproses":
        tanya = input("Status tiket sedang 'Diproses'. Masalah sudah tuntas dan ubah ke 'Selesai'? (y/n): ").strip().lower()
        if tanya == "y":
            tiket_target["status"] = "Selesai"
            print(f"Status tiket {tiket_target['kode_tiket']} diperbarui menjadi Selesai.")
