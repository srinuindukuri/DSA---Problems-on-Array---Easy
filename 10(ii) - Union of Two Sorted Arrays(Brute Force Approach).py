# Brute force Approach - Using Set
# Time complexity - O( (m+n)log(m+n) )
# Space complexity - O(m+n)

def find_union(arr1, arr2):
    s = set()  # Set --> Set Always select/ take UNIQUE element.
    union = []

    for num in arr1:
        s.add(num)

    for num in arr2:
        s.add(num)

    for num in s:
        union.append(num)

    return union


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(union)
