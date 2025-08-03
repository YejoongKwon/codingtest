# data = [5,3,4,6,18,2]

def insert_sort(A):
    for i in range(1,len(A)):
        j = i-1
        cur = A[i]
        while j >= 0 and cur < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = cur
    return A

def recursive_insert_sort(A, n):
    # Base case: if the array has only one element, it's already sorted
    if n <= 1:
        return A

    # Recursively sort the first n-1 elements
    recursive_insert_sort(A, n-1)

    # Insert the nth element into the sorted sequence
    cur = A[n-1]
    j = n-2

    # Shift elements of the sorted sequence to the right to create position for cur
    while j >= 0 and A[j] > cur:
        A[j+1] = A[j]
        j -= 1

    # Place cur at its correct position
    A[j+1] = cur

    return A

A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_A = recursive_insert_sort(A, len(A))
print(sorted_A)