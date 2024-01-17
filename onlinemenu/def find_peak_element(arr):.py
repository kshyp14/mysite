def find_max_number(arr):
    if not arr:
        return None
    
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # have to check if arr[mid] is the max number
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]

        # checking If the number to the right of mid is greater, there is a max number in the right half
        elif mid < len(arr) - 1 and arr[mid + 1] > arr[mid]:
            low = mid + 1

        # checking If the number to the left of mid is greater, there is a max number in the left half
        else:
            high = mid - 1
    

# have to check below arrays as a test cases
arr1 = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
# Output: 500
arr2 = [1, 3, 50, 10, 9, 7, 6]
# Output: 50
arr3 = [10, 20, 30, 40, 50]
 # Output: 50
arr4 = [120, 100, 80, 20, 0]
# Output: 120
arr5 = [8, 8, 8, 8]
# Output: 8
arr6 = [-7, -3,-2,-1]
# Output: -1


print("test_case_arr1", find_max_number(arr1))  
print("test_case_arr2", find_max_number(arr2))  
print("test_case_arr3", find_max_number(arr3)) 
print("test_case_arr4", find_max_number(arr4))
print("test_case_arr5", find_max_number(arr5))  
print("test_case_arr6", find_max_number(arr6)) 


