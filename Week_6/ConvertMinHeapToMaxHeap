def heapify(arr, n, i):
    # Assume i is the root of a max-heap subtree
    largest = i
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)  # recursively heapify the affected subtree

def min_max(arr):
    n = len(arr)

    # Build max-heap by applying heapify from the last non-leaf node to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr
