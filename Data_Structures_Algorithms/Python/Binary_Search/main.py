
def binary_search(arr, item):

    right = len(arr) - 1
    left = 0

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == item:
            return middle
        elif arr[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

    if left > right:
        return -1


arr = [12, 20, 25, 30, 40, 50, 60]
# item = 600 # not found
item = 50
result = binary_search(arr, item)
if result == -1:
    print("Item not found", end="")
else:
    print(f"Item found at index {result}")
