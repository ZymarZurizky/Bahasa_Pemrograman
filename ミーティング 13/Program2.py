def selection_sort(arr):
    n = len(arr)
    step = 1
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {step}: {arr}")
        step += 1

# Contoh penggunaan dengan input dari pengguna
user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")
# Mengonversi input string menjadi list of integers
arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan:", arr)

selection_sort(arr)

print("Array setelah diurutkan:", arr)
