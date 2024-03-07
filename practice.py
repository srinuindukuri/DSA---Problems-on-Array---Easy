def LinearSearch(arr, num):
    for i in range(num):
        if arr[i] == num:
            return i
    return -1


arr = [1, 3, 4, 2, 6]
num = 3
print(LinearSearch(arr, num))
