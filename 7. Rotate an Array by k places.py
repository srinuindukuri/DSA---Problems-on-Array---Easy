# "Input arr[] = [1, 2, 3, 4, 5, 6, 7], k = 2, n = 7

# 1) Store all the elements in the index range k to n in a temp array
#    temp[]=[3, 4, 5, 6, 7]
# 2) Add all the elements in the index range 0 to k in the temp array
#    arr[]=[3, 4, 5, 6, 7, 1, 2]
# 3) Copy the temp array to arr[]
#    arr[]=[3, 4, 5, 6, 7, 1, 2]

# Algorithm
#    Step 1 - Define a function to rotate the array
#    Step 2 - Declare a temporary variable
#    Step 3 - Use len() to calculate the length of the array and store it in a variable
#    Step 4 - Run a loop from k to n and store the elements at each index in the temp array
#    Step 5 - Run another loop to add the rest of the elements to the temporary array
#    Step 6 - Copy temp array to original array
#    Step 7 - Return array"

def rotateArray(a, k):
    temp = []
    n = len(a)
    for i in range(k, n):
        temp.append(a[i])
    i = 0
    for i in range(0, k):
        temp.append(a[i])
    a = temp.copy()
    return a


arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))
