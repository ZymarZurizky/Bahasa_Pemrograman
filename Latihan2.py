def input_barang():
  nama_barang = input("Masukkan nama barang: ")
  kode_barang = input("Masukkan kode barang: ")
  jumlah_barang = int(input("Masukkan jumlah barang: "))

  data_barang = {
    "nama_barang": nama_barang,
    "kode_barang": kode_barang,
    "jumlah_barang": jumlah_barang
  }

  return data_barang

def display_barang(data_barang):
  if data_barang:
    for barang in data_barang.values():
      print(f"Nama Barang: {barang['nama_barang']}")
      print(f"Kode Barang: {barang['kode_barang']}")
      print(f"Jumlah Barang: {barang['jumlah_barang']}")
      print()
  else:
    print("Data barang kosong.")

def search_barang(data_barang, kode_barang):
  barang = data_barang.get(kode_barang)
  if barang:
    print(f"Nama Barang: {barang['nama_barang']}")
    print(f"Kode Barang: {barang['kode_barang']}")
    print(f"Jumlah Barang: {barang['jumlah_barang']}")
  else:
    print(f"Barang dengan kode {kode_barang} tidak ditemukan.")

def delete_barang(data_barang, kode_barang):
  if kode_barang in data_barang:
    del data_barang[kode_barang]
    print(f"Barang dengan kode {kode_barang} telah dihapus.")
  else:
    print(f"Barang dengan kode {kode_barang} tidak ditemukan.")

data_barang = {}

while True:
  print("|================================|")
  print("|     Menu Inventaris Barang     |")
  print("|================================|")
  print("|1. Tambah Barang                |")
  print("|2. Tampilkan Semua Barang       |")
  print("|3. Cari Barang                  |")
  print("|4. Hapus Barang                 |")
  print("|5. Keluar                       |")
  print("|================================|")


  pilihan = input("Masukkan pilihan: ")

  if pilihan == "1":
    data_barang.update(input_barang())
  elif pilihan == "2":
    display_barang(data_barang)
  elif pilihan == "3":
    kode_barang = input("Masukkan kode barang: ")
    search_barang(data_barang, kode_barang)
  elif pilihan == "4":
    kode_barang = input("Masukkan kode barang: ")
    delete_barang(data_barang, kode_barang)
  elif pilihan == "5":
    break
  else:
    print("Pilihan tidak valid.")