def heapify(arr, n, i):
    smallest = i  # Initialize smallest as the root
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        heapify(arr, n, smallest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
num_elements = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)
