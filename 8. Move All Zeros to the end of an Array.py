# Method - 1: Traversing the Array
def pushZerosToEnd(arr, n):
    count = 0  # Count of non-zero elements

    for i in range(n):
        if arr[i] != 0:

            # here count is incremented
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

# -----------------------------------------------------------------
# Method - 1: Partitioning the Array
A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]  # Partitioning the array
        j += 1
print(A)
