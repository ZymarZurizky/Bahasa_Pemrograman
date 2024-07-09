def bubble_sort(arr):
    n = len(arr)
    step = 1
    # Traverse through all elements in the array
    for i in range(n):
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print(f"Step {step}: {arr}")
            step += 1
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

# Contoh penggunaan dengan input dari pengguna
user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")
# Mengonversi input string menjadi list of integers
arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan:", arr)

bubble_sort(arr)

print("Array setelah diurutkan:", arr)
