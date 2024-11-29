from datetime import datetime
daftar_tugas = []

# Fungsi untuk menambah tugas
def tambah_tugas():
    while True:
        # Input tugas
        while True:
            tugas = input("Masukkan tugas baru: ")
            if any(char.isdigit() for char in tugas):
                print("Input tidak valid. Tugas tidak boleh mengandung angka.")
            else:
                break
        
        # Input rincian
        while True:
            rincian = input("Masukkan rincian tugas (opsional): ")
            if any(char.isdigit() for char in rincian):
                print("Input tidak valid. Rincian tidak boleh mengandung angka.")
            else:
                break
        
        # Input deadline
        deadline = input("Masukkan deadline (YYYY-MM-DD, opsional): ")
        if deadline:
            try:
                deadline = datetime.strptime(deadline, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Format deadline salah. Deadline tidak ditambahkan.")
                deadline = None

        # Input tanggal tugas
        while True:
            tanggal_tugas = input("Masukkan tanggal tugas dibuat (YYYY-MM-DD): ")
            try:
                tanggal_valid = datetime.strptime(tanggal_tugas, "%Y-%m-%d")
                break
            except ValueError:
                print("Input tidak valid. Masukkan tanggal dengan format (YYYY-MM-DD).")

        # Tambahkan ke daftar
        daftar_tugas.append({
            "tugas": tugas,
            "rincian": rincian,
            "tanggal": tanggal_valid,
            "selesai": False,
            "deadline": deadline
        })

        print("Tugas berhasil ditambahkan!")
        break

# Fungsi untuk melihat daftar tugas
def lihat_tugas():
    if not daftar_tugas:
        print("Tidak ada tugas dalam daftar. Silakan tambahkan tugas terlebih dahulu.")
        return

    print("\nDaftar Tugas:")
    daftar_tugas.sort(key=lambda x: x["tanggal"])
    print(f"\nTotal Tugas: {len(daftar_tugas)}\n")

    for i, item in enumerate(daftar_tugas, start=1):
        deadline = item["deadline"] if item["deadline"] else "Tidak ada deadline"
        status = "Selesai" if item["selesai"] else "Belum selesai"
        rincian = item["rincian"] if item["rincian"] else "Tidak ada rincian"
        tanggal = item["tanggal"].strftime("%Y-%m-%d")
        print(f"{i}. {item['tugas']}")
        print(f"   Rincian: {rincian}")
        print(f"   Tanggal Dibuat: {tanggal}")
        print(f"   Deadline: {deadline}")
        print(f"   Status: {status}")

# Fungsi untuk menghapus tugas
def hapus_tugas():
    lihat_tugas()
    while True:
        try:
            nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor_tugas <= len(daftar_tugas):
                tugas_dihapus = daftar_tugas.pop(nomor_tugas - 1)
                print(f"Tugas '{tugas_dihapus['tugas']}' berhasil dihapus.")
                break
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid, masukkan nomor tugas.")

# Fungsi untuk menandai tugas selesai
def tandai_tugas_selesai():
    lihat_tugas()
    while True:
        try:
            nomor_tugas = int(input("Masukkan nomor tugas yang selesai: "))
            if 1 <= nomor_tugas <= len(daftar_tugas):
                daftar_tugas[nomor_tugas - 1]["selesai"] = True
                print("Tugas berhasil ditandai sebagai selesai.")
                break
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid, masukkan nomor tugas.")

# Fungsi untuk memperbarui tugas
def update_tugas():
    lihat_tugas()
    while True:
        try:
            nomor_tugas = int(input("Masukkan nomor tugas yang ingin diperbarui: "))
            if 1 <= nomor_tugas <= len(daftar_tugas):
                tugas_baru = input("Masukkan tugas baru (kosongkan jika tidak ingin mengubah): ")
                rincian_baru = input("Masukkan rincian baru (kosongkan jika tidak ingin mengubah): ")
                deadline_baru = input("Masukkan deadline baru (YYYY-MM-DD, kosongkan jika tidak ingin mengubah): ")
                if deadline_baru and len(deadline_baru) != 10:
                    print("Format deadline salah. Deadline tidak akan diubah.")
                    deadline_baru = "tidak ada deadline"

                if tugas_baru:
                    daftar_tugas[nomor_tugas - 1]["tugas"] = tugas_baru
                if rincian_baru:
                    daftar_tugas[nomor_tugas - 1]["rincian"] = rincian_baru
                if deadline_baru:
                    daftar_tugas[nomor_tugas - 1]["deadline"] = deadline_baru

                print("Tugas berhasil diperbarui!")
                break
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid, masukkan nomor tugas.")

# Program utama
while True:
    print("\n=== Menu To-Do List ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Update Tugas")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        tandai_tugas_selesai()
    elif pilihan == "5":
        update_tugas()
    elif pilihan == "6":
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih lagi.")