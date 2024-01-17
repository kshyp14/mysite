def find_max_number(arr):
    if not arr:
        return None
    
    max_num = arr[0]

    for num in arr:
        print("num", num)
        if num > max_num:
            max_num = num
            print("max_num", max_num)
    return max_num


# Test cases
arr1 = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
arr2 = [1, 3, 50, 10, 9, 7, 6]
arr3 = [10, 20, 30, 40, 50]
arr4 = [120, 100, 80, 20, 0]

print(find_max_number(arr1))  # Output: 500
print(find_max_number(arr2))  # Output: 50
print(find_max_number(arr3))  # Output: 50
print(find_max_number(arr4))  # Output: 120