def LinearSearch(arr, num):
    for i in range(n):
        if arr[i] == num:
            return i
    return -1


arr = [6, 7, 8, 4, 1]
n = len(arr)
num = 7
print(LinearSearch(arr, num))
