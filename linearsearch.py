

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

numbers = [5, 3, 8, 4, 2]
key = int(input("Enter the number to search: "))

result = linear_search(numbers, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
