
def linear_search(arr, item):
    for i in range(len(arr)):
        if item == arr[i]:
            return i

    return -1


arr = [20, 30, 40, 10, 55, 80, 40, 60]
item = 40
result = linear_search(arr, item)
if result == -1:
    print("Item not found")
else:
    print(f"Item found at index {result}")
