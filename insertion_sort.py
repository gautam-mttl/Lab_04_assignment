def insertion_sort(arr):
    # Traverse through all elements in the list
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [64, 25, 12, 22, 11]
insertion_sort(my_list)
print("Sorted array is:", my_list)
