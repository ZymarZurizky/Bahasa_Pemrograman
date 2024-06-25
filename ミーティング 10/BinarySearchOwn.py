def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    indices = []

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            indices.append(mid)
            left = mid - 1
            right = mid + 1
            while left >= 0 and arr[left] == x:
                indices.append(left)
                left -= 1
            while right < len(arr) and arr[right] == x:
                indices.append(right)
                right += 1
            return indices
    return -1

def main():
    while True:
        arr = list(map(int, input("Masukkan daftar elemen (pisahkan dengan spasi): ").split()))
        
        # Menyortir daftar elemen
        arr.sort()
        print(f"Daftar elemen yang sudah disortir  : {arr}")

        x = int(input("Masukkan elemen yang akan dicari: "))

        result = binary_search(arr, x)

        if result != -1:
            print(f"Elemen ditemukan pada indeks {', '.join(map(str, result))}")
        else:
            print("Elemen tidak ditemukan dalam daftar")

        ulangi = input("Apakah Anda ingin mencari elemen lain? (y/n): ").strip().lower()
        if ulangi != 'y':
            break

if __name__ == "__main__":
    main()
