def merge_sort(arr, step=1):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        merge_sort(left_half, step)
        # Sorting the second half
        merge_sort(right_half, step)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f"Step {step}: {arr}")
        step += 1

# Contoh penggunaan dengan input dari pengguna
user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")
# Mengonversi input string menjadi list of integers
arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan:", arr)

merge_sort(arr)

print("Array setelah diurutkan:", arr)
