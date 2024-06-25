class KeuanganPribadi:
    def __init__(self):
        self.transaksi = []

    def tambah_transaksi(self, jumlah, jenis):
        if jenis not in ["pemasukan", "pengeluaran"]:
            print("Jenis transaksi tidak valid. Gunakan 'pemasukan' atau 'pengeluaran'.")
            return
        self.transaksi.append({"jumlah": jumlah, "jenis": jenis})

    def tampilkan_transaksi(self):
        if not self.transaksi:
            print("Tidak ada transaksi.")
            return
        for idx, trx in enumerate(self.transaksi, start=1):
            print(f"{idx}. {trx['jenis'].capitalize()}: Rp{trx['jumlah']}")

    def hitung_total_pemasukan(self):
        total_pemasukan = sum(trx['jumlah'] for trx in self.transaksi if trx['jenis'] == "pemasukan")
        print(f"Total Pemasukan: Rp{total_pemasukan}")
        return total_pemasukan

    def hitung_total_pengeluaran(self):
        total_pengeluaran = sum(trx['jumlah'] for trx in self.transaksi if trx['jenis'] == "pengeluaran")
        print(f"Total Pengeluaran: Rp{total_pengeluaran}")
        return total_pengeluaran

    def hitung_saldo_akhir(self):
        saldo_akhir = self.hitung_total_pemasukan() - self.hitung_total_pengeluaran()
        print(f"Saldo Akhir: Rp{saldo_akhir}")
        return saldo_akhir

keuangan = KeuanganPribadi()

keuangan.tambah_transaksi(500000, "pemasukan")
keuangan.tambah_transaksi(200000, "pengeluaran")
keuangan.tambah_transaksi(100000, "pemasukan")

print("\nSemua Transaksi:")
keuangan.tampilkan_transaksi()

print("\nMenghitung Total Pemasukan:")
keuangan.hitung_total_pemasukan()

print("\nMenghitung Total Pengeluaran:")
keuangan.hitung_total_pengeluaran()

print("\nMenghitung Saldo Akhir:")
keuangan.hitung_saldo_akhir()
