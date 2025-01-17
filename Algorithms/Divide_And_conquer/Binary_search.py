'''
Divide the search space into two halves by finding the middle index “mid”. 
1. Compare the middle element of the search space with the key. 
2.If the key is found at middle element, the process is terminated.
3. If the key is not found at middle element, choose which half will be used as the next search space.
4. If the key is smaller than the middle element, then the left side is used for next search.
5. If the key is larger than the middle element, then the right side is used for next search.
6. This process is continued until the key is found or the total search space is exhausted.


'''


def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
  
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
