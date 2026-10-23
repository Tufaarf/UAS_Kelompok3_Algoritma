"""
Fitur 2: Tampilkan Daftar Tiket (Native Python)
Deskripsi: Staf / Pengguna dapat melihat daftar tiket yang tersimpan dalam sistem.
"""

def penanda(nilai):
    """Mengubah nilai menjadi penanda visual uppercase, misal 'Tinggi' -> '[TINGGI]'."""
    return f"[{str(nilai).upper()}]"


def lihat_daftar_tiket(daftar_tiket):
    """
    Menampilkan SEMUA tiket dalam sistem (digunakan oleh Admin).
    Kolom: No, Kode, Nama Pelapor, Jenis Masalah, Prioritas, Status.
    Dilengkapi ringkasan jumlah status di bagian bawah tabel.
    """
    print("\n--- DAFTAR SEMUA TIKET (ADMIN) ---")

    if not daftar_tiket:
        print("Belum ada tiket dalam sistem.")
        return

    w_no, w_kode, w_nama, w_jenis, w_prio, w_status = 4, 10, 22, 18, 12, 14
    garis = "-" * (w_no + w_kode + w_nama + w_jenis + w_prio + w_status + (5 * 3))

    print(garis)
    print(
        f"{'No':<{w_no}} | {'Kode':<{w_kode}} | {'Nama Pelapor':<{w_nama}} | "
        f"{'Jenis Masalah':<{w_jenis}} | {'Prioritas':<{w_prio}} | {'Status':<{w_status}}"
    )
    print(garis)

    for i, t in enumerate(daftar_tiket, start=1):
        nama = t["nama_pelapor"]
        nama_fmt = (nama[:19] + "...") if len(nama) > w_nama else nama
        jenis = t["jenis_masalah"]
        jenis_fmt = (jenis[:15] + "...") if len(jenis) > w_jenis else jenis

        print(
            f"{i:<{w_no}} | {t['kode_tiket']:<{w_kode}} | {nama_fmt:<{w_nama}} | "
            f"{jenis_fmt:<{w_jenis}} | {penanda(t['prioritas']):<{w_prio}} | "
            f"{penanda(t['status']):<{w_status}}"
        )
    print(garis)

    # Ringkasan di bagian bawah tabel
    total = len(daftar_tiket)
    menunggu = sum(1 for t in daftar_tiket if t["status"].lower() == "menunggu")
    diproses = sum(1 for t in daftar_tiket if t["status"].lower() == "diproses")
    selesai = sum(1 for t in daftar_tiket if t["status"].lower() == "selesai")

    print(f"Total tiket : {total}")
    print(f"Menunggu    : {menunggu}")
    print(f"Diproses    : {diproses}")
    print(f"Selesai     : {selesai}")


def lihat_tiket_user(daftar_tiket, nama_user):
    """
    Menampilkan hanya tiket milik user yang sedang aktif.
    Format tabel rapi dengan ringkasan status tiket milik user tersebut.
    """
    print(f"\n--- DAFTAR TIKET SAYA ({nama_user}) ---")

    # Filter tiket yang dimiliki user (case-insensitive)
    tiket_user = [
        t for t in daftar_tiket
        if t["nama_pelapor"].strip().lower() == nama_user.strip().lower()
    ]

    if not tiket_user:
        print("Anda belum memiliki tiket yang diajukan.")
        return

    w_no, w_kode, w_jenis, w_prio, w_status = 4, 10, 18, 12, 14
    garis = "-" * (w_no + w_kode + w_jenis + w_prio + w_status + (4 * 3))

    print(garis)
    print(
        f"{'No':<{w_no}} | {'Kode':<{w_kode}} | {'Jenis Masalah':<{w_jenis}} | "
        f"{'Prioritas':<{w_prio}} | {'Status':<{w_status}}"
    )
    print(garis)

    for i, t in enumerate(tiket_user, start=1):
        jenis = t["jenis_masalah"]
        jenis_fmt = (jenis[:15] + "...") if len(jenis) > w_jenis else jenis

        print(
            f"{i:<{w_no}} | {t['kode_tiket']:<{w_kode}} | {jenis_fmt:<{w_jenis}} | "
            f"{penanda(t['prioritas']):<{w_prio}} | {penanda(t['status']):<{w_status}}"
        )
    print(garis)

    total = len(tiket_user)
    menunggu = sum(1 for t in tiket_user if t["status"].lower() == "menunggu")
    diproses = sum(1 for t in tiket_user if t["status"].lower() == "diproses")
    selesai = sum(1 for t in tiket_user if t["status"].lower() == "selesai")

    print(f"Total tiket saya : {total}")
    print(f"Menunggu         : {menunggu}")
    print(f"Diproses         : {diproses}")
    print(f"Selesai          : {selesai}")
