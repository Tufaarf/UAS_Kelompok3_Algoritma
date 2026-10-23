"""
MASTER FILE: Sistem Helpdesk / Tiket Layanan (Tahap 1 - Array & Struct)
Mata Kuliah: Algoritma dan Struktur Data

100% Native Python tanpa library eksternal.
Mendukung 2 tipe peran:
1. User / Pelapor: Menambah tiket baru dan mengelola (melihat, cek respon, membatalkan) tiket miliknya sendiri.
2. Admin / Staf Helpdesk: Mengelola seluruh tiket, memperbarui status, menjawab tiket, filter, dan hapus tiket.
"""

from function.utils import clear_screen, jeda
from function.add import tambah_tiket
from function.tiket import lihat_daftar_tiket, lihat_tiket_user
from function.search import menu_cari_tiket, cari_tiket_user
from function.update import update_status_tiket, jawab_tiket
from function.filter import filter_tiket
from function.delete import hapus_tiket, batalkan_tiket_user


def menu_user_portal(daftar_tiket):
    """Portal khusus pengguna / pelapor."""
    clear_screen()
    print("=" * 55)
    print("                 MASUK SEBAGAI USER                ")
    print("=" * 55)
    nama_user = input("Masukkan Nama Anda: ").strip()
    if not nama_user:
        print("[Error] Nama tidak boleh kosong.")
        jeda("Tekan Enter untuk kembali ke menu peran...")
        return

    while True:
        clear_screen()
        print("=" * 55)
        print(f"   PORTAL USER - HELPDESK (User: {nama_user})   ")
        print("=" * 55)
        print("1. Tambah Tiket Baru")
        print("2. Lihat Daftar Tiket Saya")
        print("3. Lihat Detail & Tanggapan Tiket Saya")
        print("4. Batalkan / Hapus Tiket Saya")
        print("0. Kembali ke Menu Peran")
        print("=" * 55)

        pilihan = input("Pilih menu (0-4): ").strip()

        if pilihan == "1":
            clear_screen()
            tambah_tiket(daftar_tiket, nama_pelapor_default=nama_user)
            jeda()
        elif pilihan == "2":
            clear_screen()
            lihat_tiket_user(daftar_tiket, nama_user)
            jeda()
        elif pilihan == "3":
            clear_screen()
            cari_tiket_user(daftar_tiket, nama_user)
            jeda()
        elif pilihan == "4":
            clear_screen()
            batalkan_tiket_user(daftar_tiket, nama_user)
            jeda()
        elif pilihan == "0":
            break
        else:
            print("\n[Error] Pilihan tidak valid. Silakan pilih angka 0 sampai 4.")
            jeda("Tekan Enter untuk mencoba lagi...")


def menu_admin_portal(daftar_tiket):
    """Panel khusus Admin / Staf Helpdesk."""
    while True:
        clear_screen()
        print("=" * 55)
        print("           PANEL ADMIN / STAF HELPDESK           ")
        print("=" * 55)
        print("1. Tampilkan Semua Tiket")
        print("2. Cari Tiket (Kode / Nama Pelapor)")
        print("3. Update Status Tiket (Alur Satu Arah)")
        print("4. Jawab / Beri Tanggapan Tiket")
        print("5. Filter Tiket Berdasarkan Jenis Masalah")
        print("6. Tambah Tiket Baru")
        print("7. Hapus Tiket (Khusus Status Selesai)")
        print("0. Kembali ke Menu Peran")
        print("=" * 55)

        pilihan = input("Pilih menu (0-7): ").strip()

        if pilihan == "1":
            clear_screen()
            lihat_daftar_tiket(daftar_tiket)
            jeda()
        elif pilihan == "2":
            clear_screen()
            menu_cari_tiket(daftar_tiket)
            jeda()
        elif pilihan == "3":
            clear_screen()
            update_status_tiket(daftar_tiket)
            jeda()
        elif pilihan == "4":
            clear_screen()
            jawab_tiket(daftar_tiket)
            jeda()
        elif pilihan == "5":
            clear_screen()
            filter_tiket(daftar_tiket)
            jeda()
        elif pilihan == "6":
            clear_screen()
            tambah_tiket(daftar_tiket)
            jeda()
        elif pilihan == "7":
            clear_screen()
            hapus_tiket(daftar_tiket)
            jeda()
        elif pilihan == "0":
            break
        else:
            print("\n[Error] Pilihan tidak valid. Silakan pilih angka 0 sampai 7.")
            jeda("Tekan Enter untuk mencoba lagi...")


def main():
    """
    Fungsi utama program.
    Menyimpan koleksi data tiket dalam memori (Array of Struct / List of Dict).
    Menyediakan alur pemilihan peran (User vs Admin).
    """
    # Seluruh data tiket disimpan di memori program (Array of Struct)
    daftar_tiket = []

    while True:
        try:
            clear_screen()
            print("=" * 55)
            print("        SISTEM HELPDESK / TIKET LAYANAN (CLI)      ")
            print("=" * 55)
            print("Pilih Peran Anda:")
            print("1. Masuk sebagai User / Pelapor")
            print("2. Masuk sebagai Admin / Staf Helpdesk")
            print("0. Keluar dari Program")
            print("=" * 55)

            peran = input("Pilih peran (0-2): ").strip()

            if peran == "1":
                menu_user_portal(daftar_tiket)
            elif peran == "2":
                menu_admin_portal(daftar_tiket)
            elif peran == "0":
                clear_screen()
                print("=" * 55)
                print("Terima kasih telah menggunakan Sistem Helpdesk.")
                print("Sampai jumpa!")
                print("=" * 55)
                break
            else:
                print("\n[Error] Pilihan peran tidak valid. Masukkan 1, 2, atau 0.")
                jeda("Tekan Enter untuk mencoba lagi...")
        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram dihentikan oleh pengguna. Sampai jumpa!")
            break


if __name__ == "__main__":
    main()