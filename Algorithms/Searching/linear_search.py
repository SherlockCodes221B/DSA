arr = [1,10,32,1,23,98,100,54,32,33,87]
target = 98

def search(arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


result = search(arr)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")