# Program Perpustakaan

# Dictionary untuk menyimpan data buku
buku = {}

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    harga = int(input("Masukkan harga buku: "))
    buku[judul] = {"penulis": penulis, "harga": harga}
    print("\033[1;32m\nBuku berhasil ditambahkan!\033[0m")

def tampilkan_semua_buku():
    if buku:
        print("\nDaftar buku:")
        # Pengurutan data berdasarkan judul buku
        daftar_buku = sorted(buku.items())
        for i, (judul, data) in enumerate(daftar_buku):
            print(f"{i+1}. {judul} oleh {data['penulis']} - Rp {data['harga']}")
    else:
        print("Tidak ada buku di perpustakaan.")

def cari_buku():
    keyword = input("Masukkan keyword untuk mencari buku: ")
    hasil = []
    for judul, data in buku.items():
        if keyword in judul or keyword in data["penulis"] or str(data["harga"]) == keyword:
            hasil.append((judul, data["penulis"], data["harga"]))
    if hasil:
        print("Hasil pencarian:")
        # Pengurutan data berdasarkan judul buku
        hasil.sort(key=lambda x: x[0])
        for i, (judul, penulis, harga) in enumerate(hasil):
            print(f"{i+1}. {judul} oleh {penulis} - Rp {harga}")
    else:
        print("Tidak ditemukan buku yang sesuai.")

def hapus_buku():
    print("Daftar Buku:")
    for i, (judul, detail) in enumerate(buku.items(), 1):
        print(f"{i}. {judul} - {detail['penulis']} (Rp {detail['harga']})")

    while True:
        try:
            nomor = int(input("Masukkan nomor buku yang ingin dihapus: "))
            if nomor < 1 or nomor > len(buku):
                print("\033[1;31mInput tidak valid. Silakan masukkan nomor.\033[0m")
                continue
            judul = list(buku.keys())[nomor - 1]
            del buku[judul]
            print("\033[1;32mBuku berhasil dihapus!\033[0m")
            break
        except ValueError:
            print("\033[1;31mInput tidak valid. Silakan masukkan nomor.\033[0m")

def edit_buku():
    judul = input("Masukkan judul buku yang ingin diedit: ")
    if judul in buku:
        print("Data buku saat ini:")
        print(f"Judul: {judul}")
        print(f"Penulis: {buku[judul]['penulis']}")
        print(f"Harga: Rp {buku[judul]['harga']}")
        penulis_baru = input("Masukkan penulis baru (kosongkan jika tidak ingin mengubah): ")
        harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
        if penulis_baru:
            buku[judul]["penulis"] = penulis_baru
        if harga_baru:
            buku[judul]["harga"] = int(harga_baru)
        print("Data buku berhasil diedit!")
    else:
        print("Buku tidak ditemukan.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambahkan buku")
        print("2. Tampilkan semua buku")
        print("3. Cari buku")
        print("4. Hapus buku")
        print("5. Edit buku")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_semua_buku()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            edit_buku()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()