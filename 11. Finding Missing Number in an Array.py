# Summation Approach:
# The steps are as follows:

# 1) We will first calculate the summation of first N natural numbers(i.e. 1 to N) using the specified formula.
# 2) Then we will add all the array elements using a loop.
# 3) Finally, we will consider the difference between the summation of the first N natural numbers and the sum of the array elements.

def Missing_number(arr, n):
    total_sum = n*(n+1) // 2
    s2 = sum(arr)
    Missing_number = total_sum - s2
    return Missing_number


arr = [1, 2, 4, 5]
n = 5
print(Missing_number(arr, n))

# -------------------------------------------------------------------------------------------------------------------------------------
# XOR Approach:
# The steps are as follows:

# 1) We will first run a loop(say i) from 0 to N-2(as the length of the array=N-1).
# 2) Inside the loop, xor2 variable will calculate the XOR of array elements i.e. xor2 = xor2 ^ a[i].
#    And the xor1 variable will calculate the XOR of 1 to N-1 i.e. xor1 = xor1 ^ (i+1).
# 3) After the loop ends we will XOR xor1 and N to get the total XOR of 1 to N.
# 4) Finally, the answer will be the XOR of xor1 and xor2.


def Missing_Number(arr, n):
    xor1 = 0
    xor2 = 0

    for i in range(n-1):
        xor2 = xor2 ^ arr[i]
        xor1 = xor1 ^ (i+1)
    xor1 = xor1 ^ n
    return xor1 ^ xor2


arr = [1, 2, 4, 5]
n = 5
print(Missing_Number(arr, n))
