"""
Fitur 5: Filter Tiket Berdasarkan Jenis Masalah
Deskripsi: Staf dapat menampilkan daftar tiket yang difilter berdasarkan jenis masalah tertentu,
memudahkan pemantauan tiket per kategori.
"""

JENIS_MASALAH_PILIHAN = {
    "1": "Hardware",
    "2": "Software",
    "3": "Jaringan",
    "4": "Lainnya",
    "hardware": "Hardware",
    "software": "Software",
    "jaringan": "Jaringan",
    "lainnya": "Lainnya"
}


def filter_tiket(daftar_tiket):
    """
    Menampilkan daftar tiket yang difilter berdasarkan jenis masalah.
    Pilihan yang valid: Hardware, Software, Jaringan, Lainnya.
    """
    print("\n--- FITUR 5: FILTER TIKET BERDASARKAN JENIS MASALAH ---")
    print("Pilihan Jenis Masalah:")
    print("  1. Hardware")
    print("  2. Software")
    print("  3. Jaringan")
    print("  4. Lainnya")

    pilihan = input("Pilih jenis masalah (1-4 atau ketik nama jenis): ").strip()

    # Validasi 1 & 2: Pilihan jenis masalah hanya boleh Hardware, Software, Jaringan, Lainnya (tidak case-sensitive)
    if pilihan.lower() not in JENIS_MASALAH_PILIHAN:
        print("[Error] Pilihan jenis masalah tidak valid! Hanya boleh: Hardware, Software, Jaringan, atau Lainnya.")
        return

    jenis_terpilih = JENIS_MASALAH_PILIHAN[pilihan.lower()]

    # Filter data dari daftar_tiket (Array of Struct / List of Dict)
    hasil = [
        t for t in daftar_tiket
        if t["jenis_masalah"].strip().lower() == jenis_terpilih.lower()
    ]

    # Output (tidak ada data)
    if not hasil:
        print(f"Tidak ada tiket dengan jenis masalah '{jenis_terpilih}' dalam sistem.")
        return

    # Output (ada data)
    print(f"\nMenampilkan tiket jenis masalah: {jenis_terpilih} ({len(hasil)} tiket ditemukan).")

    # Lebar kolom sama seperti Fitur 2
    w_no, w_kode, w_nama, w_jenis, w_prio, w_status = 4, 10, 22, 18, 12, 14
    garis = "-" * (w_no + w_kode + w_nama + w_jenis + w_prio + w_status + (5 * 3))

    print(garis)
    print(
        f"{'No':<{w_no}} | {'Kode':<{w_kode}} | {'Nama Pelapor':<{w_nama}} | "
        f"{'Jenis Masalah':<{w_jenis}} | {'Prioritas':<{w_prio}} | {'Status':<{w_status}}"
    )
    print(garis)
    for idx, tiket in enumerate(hasil, start=1):
        nama = tiket["nama_pelapor"]
        nama_fmt = (nama[:19] + "...") if len(nama) > w_nama else nama
        jenis = tiket["jenis_masalah"]
        jenis_fmt = (jenis[:15] + "...") if len(jenis) > w_jenis else jenis
        prioritas = f"[{tiket['prioritas'].upper()}]"
        status = f"[{tiket['status'].upper()}]"

        print(
            f"{idx:<{w_no}} | {tiket['kode_tiket']:<{w_kode}} | {nama_fmt:<{w_nama}} | "
            f"{jenis_fmt:<{w_jenis}} | {prioritas:<{w_prio}} | {status:<{w_status}}"
        )
    print(garis)
