class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

def input_mahasiswa():
    """Meminta input data mahasiswa dari pengguna dan mengembalikan objek Mahasiswa."""
    nama = input("\nMasukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan prodi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    return Mahasiswa(nama, nim, prodi, nilai)

def tampilkan_mahasiswa(mahasiswa):
    """Menampilkan data mahasiswa."""
    print("Nama:", mahasiswa.nama)
    print("NIM:", mahasiswa.nim)
    print("Prodi:", mahasiswa.prodi)
    print("Nilai:", mahasiswa.nilai)

def hitung_rata_rata(mahasiswa_list):
    """ Menghitung rata-rata nilai mahasiswa."""
    total_nilai = 0
    for mahasiswa in mahasiswa_list:
        total_nilai += mahasiswa.nilai
    if len(mahasiswa_list) > 0:
        rata_rata = total_nilai / len(mahasiswa_list)
        print("Rata-rata nilai mahasiswa:", rata_rata)
    else:
        print("Tidak ada data mahasiswa.")

def cari_nilai_tertinggi(mahasiswa_list):
    """Mencari dan menampilkan mahasiswa dengan nilai tertinggi."""
    if len(mahasiswa_list) > 0:
        nilai_tertinggi = mahasiswa_list[0].nilai
        mahasiswa_tertinggi = mahasiswa_list[0]
        for mahasiswa in mahasiswa_list:
            if mahasiswa.nilai > nilai_tertinggi:
                nilai_tertinggi = mahasiswa.nilai
                mahasiswa_tertinggi = mahasiswa
        print("Mahasiswa dengan nilai tertinggi:")
        tampilkan_mahasiswa(mahasiswa_tertinggi)
    else:
        print("Tidak ada data mahasiswa.")

def cari_nilai_terendah(mahasiswa_list):
    """Mencari dan menampilkan mahasiswa dengan nilai terendah."""
    if len(mahasiswa_list) > 0:
        nilai_terendah = mahasiswa_list[0].nilai
        mahasiswa_terendah = mahasiswa_list[0]
        for mahasiswa in mahasiswa_list:
            if mahasiswa.nilai < nilai_terendah:
                nilai_terendah = mahasiswa.nilai
                mahasiswa_terendah = mahasiswa
        print("\nMahasiswa dengan nilai terendah:")
        tampilkan_mahasiswa(mahasiswa_terendah)
    else:
        print("Tidak ada data mahasiswa.")

mahasiswa_list = []

while True:
    print("\nMenu:")
    print("1. Input data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hitung rata-rata nilai")
    print("4. Cari mahasiswa dengan nilai tertinggi")
    print("5. Cari mahasiswa dengan nilai terendah")
    print("6. Keluar")

    pilihan = input("\nMasukkan pilihan Anda: ")

    if pilihan == '1':
        mahasiswa = input_mahasiswa()
        mahasiswa_list.append(mahasiswa)
        print("Data mahasiswa berhasil disimpan.")
    elif pilihan == '2':
        if len(mahasiswa_list) > 0:
            print("\nData mahasiswa:")
            for mahasiswa in mahasiswa_list:
                tampilkan_mahasiswa(mahasiswa)
                print("-" * 20)
        else:
            print("Tidak ada data mahasiswa.")
    elif pilihan == '3':
        hitung_rata_rata(mahasiswa_list)
    elif pilihan == '4':
        cari_nilai_tertinggi(mahasiswa_list)
    elif pilihan == '5':
        cari_nilai_terendah(mahasiswa_list)
    elif pilihan == '6':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")