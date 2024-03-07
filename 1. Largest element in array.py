def largest_element(arr):
    max_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    print(max_element)


arr = [1, 5, 2, 7, 9, 3]
largest_element(arr)
