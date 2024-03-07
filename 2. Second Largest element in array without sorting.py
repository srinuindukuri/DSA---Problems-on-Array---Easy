
def second_largest_element(arr):
    largest = arr[0]
    slargest = arr[-1]
    for i in range(len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        else:
            arr[i] > slargest and arr[i] != largest
    return slargest


arr = [10, 20, 4, 45, 99]
print(second_largest_element(arr))
