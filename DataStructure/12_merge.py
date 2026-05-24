# Merge Sort Program

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


# User input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sorting
sorted_numbers = merge_sort(numbers)

# Output
print("Sorted Array:", sorted_numbers)