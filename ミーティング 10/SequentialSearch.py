def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    while True:
        arr = list(map(int, input("Masukkan daftar elemen (pisahkan dengan spasi): ").split()))

        x = int(input("Masukkan elemen yang akan dicari: "))

        result = sequential_search(arr, x)

        if result != -1:
            print(f"Elemen ditemukan pada indeks {result}")
        else:
            print("Elemen tidak ditemukan dalam daftar")

        ulangi = input("Apakah Anda ingin mencari elemen lain? (y/n): ").strip().lower()
        if ulangi != 'y':
            break

if __name__ == "__main__":
    main()
