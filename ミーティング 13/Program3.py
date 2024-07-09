def insertion_sort(arr):
    step = 1
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Step {step}: {arr}")
        step += 1

# Contoh penggunaan dengan input dari pengguna
user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")
# Mengonversi input string menjadi list of integers
arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan:", arr)

insertion_sort(arr)

print("Array setelah diurutkan:", arr)
