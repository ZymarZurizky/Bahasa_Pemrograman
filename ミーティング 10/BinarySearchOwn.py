def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list)

    while left < right:
        middle = (left + right) // 2
        if sorted_list[middle] == target:
            return middle
        elif sorted_list[middle] < target:
            left = middle + 1
        else:
            right = middle

    return None

def main():
    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    index = binary_search(sorted_data, target)
    if index is not None:
        print(f"Elemen {target} ditemukan di indeks {index}.")
    else:
        print(f"Elemen {target} tidak ditemukan dalam daftar.")

if __name__ == "__main__":
    main()