
def second_smallest_element(arr):
    small = arr[0]
    secondSmall = arr[0]

    for i in range(len(arr)):
        if small > arr[i]:
            small = arr[i]

    for i in range(len(arr)):
        if secondSmall > arr[i]:
            if arr[i] != small:
                secondSmall = arr[i]
    return secondSmall


arr = [10, 20, 4, 45, 99]
print(second_smallest_element(arr))
