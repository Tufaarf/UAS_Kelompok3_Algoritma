"""
Modul Utilitas: Fungsi pembersih layar CLI (clear screen) dan jeda interaksi.
100% Native Python tanpa library eksternal.
"""

import os


def clear_screen():
    """
    Membersihkan layar terminal / konsol CLI (kompatibel Windows, Linux, dan macOS).
    Menghilangkan menu lama dan riwayat tampilan agar CLI tetap bersih dan rapi.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Alias fungsi dalam bahasa Indonesia
bersihkan_layar = clear_screen


def jeda(pesan="\nTekan Enter untuk kembali ke menu..."):
    """
    Menahan tampilan agar pengguna dapat membaca output/informasi sebelum layar dibersihkan.
    Mendukung penanganan KeyboardInterrupt / EOFError secara aman.
    """
    try:
        input(pesan)
    except (KeyboardInterrupt, EOFError):
        pass
