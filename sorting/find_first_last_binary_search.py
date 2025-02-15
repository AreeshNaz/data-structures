def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_first_and_last(arr, target):
    first = binary_search_first(arr, target)
    if first == -1:  
        return [-1, -1]
    last = binary_search_last(arr, target)
    return [first, last]

# Test cases
test_cases = [
    ([0, 1, 2, 3, 3, 3, 3, 4, 5, 6], 3),  
    ([0, 1, 2, 3, 4, 5], 5),               
    ([0, 1, 2, 3, 4, 5], 6),               
]

for input_list, number in test_cases:
    result = find_first_and_last(input_list, number)
    print(f"input_list = {input_list}, number = {number} => output = {result}")
