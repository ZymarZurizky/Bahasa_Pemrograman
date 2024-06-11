class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

def input_data():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan prodi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    return Mahasiswa(nama, nim, prodi, nilai)

def tampilkan_data(mahasiswa_list):
    for mahasiswa in mahasiswa_list:
        print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Prodi: {mahasiswa.prodi}, Nilai: {mahasiswa.nilai}")

def hitung_rata_rata(mahasiswa_list):
    total_nilai = sum(mahasiswa.nilai for mahasiswa in mahasiswa_list)
    rata_rata = total_nilai / len(mahasiswa_list)
    return rata_rata

def cari_mahasiswa_nilai_tertinggi(mahasiswa_list):
    nilai_tertinggi = max(mahasiswa_list, key=lambda m: m.nilai)
    return nilai_tertinggi

def cari_mahasiswa_nilai_terendah(mahasiswa_list):
    nilai_terendah = min(mahasiswa_list, key=lambda m: m.nilai)
    return nilai_terendah

def main():
    mahasiswa_list = []
    while True:
        print("========================================")
        print("\033[1m|\033[0m                \033[1mMenu\033[0m                  \033[1m|\033[0m")
        print("========================================")
        print("\033[1m1\033[0m. Input data mahasiswa                 ")
        print("\033[1m2\033[0m. Tampilkan data mahasiswa             ")
        print("\033[1m3\033[0m. Hitung rata-rata nilai mahasiswa     ")
        print("\033[1m4\033[0m. Cari mahasiswa dengan nilai tertinggi")
        print("\033[1m5\033[0m. Cari mahasiswa dengan nilai terendah ")
        print("\033[94m\033[1m6. Keluar\033[0m")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            mahasiswa = input_data()
            mahasiswa_list.append(mahasiswa)
        elif pilihan == '2':
            tampilkan_data(mahasiswa_list)
        elif pilihan == '3':
            if mahasiswa_list:
                rata_rata = hitung_rata_rata(mahasiswa_list)
                print(f"Rata-rata nilai mahasiswa: {rata_rata}")
            else:
                print("Tidak ada data mahasiswa.")
        elif pilihan == '4':
            if mahasiswa_list:
                mahasiswa_tertinggi = cari_mahasiswa_nilai_tertinggi(mahasiswa_list)
                print(f"Mahasiswa dengan nilai tertinggi: {mahasiswa_tertinggi.nama}, Nilai: {mahasiswa_tertinggi.nilai}")
            else:
                print("Tidak ada data mahasiswa.")
        elif pilihan == '5':
            if mahasiswa_list:
                mahasiswa_terendah = cari_mahasiswa_nilai_terendah(mahasiswa_list)
                print(f"Mahasiswa dengan nilai terendah: {mahasiswa_terendah.nama}, Nilai: {mahasiswa_terendah.nilai}")
            else:
                print("Tidak ada data mahasiswa.")
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()