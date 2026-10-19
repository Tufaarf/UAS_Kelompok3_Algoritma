import os

def bersihkan_layar():
    """Clear terminal screen untuk Windows (cls) maupun Linux/Mac (clear)."""
    os.system("cls" if os.name == "nt" else "clear")
    
def filter_tiket(daftar_tiket):
        """Fitur 5 (Extended): Memfilter tiket berdasarkan Jenis Masalah, Prioritas, atau Status."""
        bersihkan_layar()
        print("=" * 75)
        print("                           FILTER TIKET                            ")
        print("=" * 75)

        if not daftar_tiket:
            print("\n[Info] Belum ada tiket dalam sistem.")
            print("=" * 75)
            input("\nTekan Enter untuk kembali ke menu utama...")
            bersihkan_layar()
            return

        # 1. Pilih Kriteria Filter
        print("Pilih Kriteria Filter:")
        print("  1. Filter Berdasarkan Jenis Masalah")
        print("  2. Filter Berdasarkan Prioritas")
        print("  3. Filter Berdasarkan Status")
        print("  0. Batal / Kembali ke Menu Utama")

        while True:
            pilihan_kriteria = input("\nPilih angka (0-3): ").strip()
            if pilihan_kriteria in ["0", "1", "2", "3"]:
                break
            print("[Error] Pilihan tidak valid, masukkan angka 0 sampai 3!")

        if pilihan_kriteria == "0":
            bersihkan_layar()
            return

        # Pemetaan Kriteria ke Opsi & Key Dictionary
        if pilihan_kriteria == "1":
            judul_kriteria = "Jenis Masalah"
            daftar_opsi = JENIS_MASALAH_OPSI
            kunci_dict = "jenis_masalah"
        elif pilihan_kriteria == "2":
            judul_kriteria = "Prioritas"
            daftar_opsi = PRIORITAS_OPSI
            kunci_dict = "prioritas"
        elif pilihan_kriteria == "3":
            judul_kriteria = "Status"
            daftar_opsi = STATUS_OPSI
            kunci_dict = "status"

        # 2. Tampilkan Nilai Pilihan dari Kriteria Terpilih
        print(f"\nPilih Nilai {judul_kriteria} yang ingin difilter:")
        for idx, opsi in enumerate(daftar_opsi, 1):
            print(f"  {idx}. {opsi}")

        while True:
            pilihan_nilai = input(f"Pilih angka (1-{len(daftar_opsi)}): ").strip()
            if pilihan_nilai.isdigit():
                idx_pilih = int(pilihan_nilai) - 1
                if 0 <= idx_pilih < len(daftar_opsi):
                    nilai_terpilih = daftar_opsi[idx_pilih]
                    break
            print("[Error] Pilihan tidak valid, masukkan angka yang tersedia!")

        # 3. Proses Filtering
        if kunci_dict == "jenis_masalah":
            # Substring match untuk menangani custom 'Lainnya (detail)'
            hasil = [
                t for t in daftar_tiket
                if nilai_terpilih.lower() in t.get(kunci_dict, "").lower()
            ]
        else:
            # Exact match (case-insensitive) untuk Prioritas dan Status
            hasil = [
                t for t in daftar_tiket
                if t.get(kunci_dict, "").strip().lower() == nilai_terpilih.lower()
            ]

        # 4. Tampilkan Hasil Filter
        print("\n" + "=" * 75)
        if hasil:
            print(f"Menampilkan tiket dengan {judul_kriteria}: '{nilai_terpilih}' ({len(hasil)} tiket ditemukan):")
            print("-" * 75)
            print(f"{'NO':<4} | {'KODE':<8} | {'NAMA PELAPOR':<18} | {'JENIS MASALAH':<16} | {'PRIORITAS':<10} | {'STATUS':<11}")
            print("-" * 75)
            for idx, tiket in enumerate(hasil, 1):
                kode = tiket.get("kode_tiket", "-")
                nama = tiket.get("nama_pelapor", "-")
                nama_fmt = (nama[:15] + "...") if len(nama) > 18 else nama
                jenis = tiket.get("jenis_masalah", "-")
                jenis_fmt = (jenis[:13] + "...") if len(jenis) > 16 else jenis
                prio_fmt = f"[{tiket.get('prioritas', '-').upper()}]"
                status_fmt = f"[{tiket.get('status', '-').upper()}]"

                print(f"{idx:<4} | {kode:<8} | {nama_fmt:<18} | {jenis_fmt:<16} | {prio_fmt:<10} | {status_fmt:<11}")
            print("=" * 75)
        else:
            print(f"[Info] Tidak ada tiket dengan {judul_kriteria} '{nilai_terpilih}' dalam sistem.")
            print("=" * 75)

        input("\nTekan Enter untuk kembali ke menu utama...")
        bersihkan_layar()