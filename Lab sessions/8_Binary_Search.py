def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2   

        if arr[mid] == target:
            return mid            
        elif arr[mid] < target:
            low = mid + 1         
        else:
            high = mid - 1        
    return -1   

numbers = [2, 4, 6, 8, 10, 12, 14]
x = 11

result = binary_search(numbers, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found")