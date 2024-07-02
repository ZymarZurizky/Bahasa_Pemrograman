def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    indices = []

    while low <= high:
        mid = (high + low) // 2

        # Jika elemen berada di tengah
        if arr[mid] < x:
            low = mid + 1

        # Jika elemen berada di sebelah kiri tengah
        elif arr[mid] > x:
            high = mid - 1

        # Elemen ditemukan
        else:
            indices.append(mid)
            # Cari elemen duplikat di sebelah kiri dan kanan
            left = mid - 1
            right = mid + 1
            while left >= 0 and arr[left] == x:
                indices.append(left)
                left -= 1
            while right < len(arr) and arr[right] == x:
                indices.append(right)
                right += 1
            return indices

    # Elemen tidak ditemukan
    return -1

def main():
    while True:
        # Menerima input daftar elemen yang sudah terurut dari pengguna
        arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))

        # Menerima input elemen yang akan dicari
        x = int(input("Masukkan elemen yang akan dicari: "))

        result = binary_search(arr, x)

        if result!= -1:
            print(f"Elemen ditemukan pada indeks {', '.join(map(str, result))}")
        else:
            print("Elemen tidak ditemukan dalam daftar")

        # Menanyakan apakah pengguna ingin mengulangi
        ulangi = input("Apakah Anda ingin mencari elemen lain? (y/n): ").strip().lower()
        if ulangi!= 'y':
            break

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()