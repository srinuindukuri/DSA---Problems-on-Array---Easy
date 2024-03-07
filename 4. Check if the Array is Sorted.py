def sorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True


arr = [1, 2, 1, 3, 4]
n = 5
print(sorted(arr, n))
