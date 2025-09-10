def select_sort(array):
    n = len(array)

    for i in range(n-1):
        lst = i
        for j in range(i+1, n):
            if array[lst]>array[j]:
                lst = j

        array[i], array[lst] = array[lst], array[i]

    return array
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1]= temp
    return array

def quicksort(array, start, end):
    if start >= end:
        return

    pivot = start
    left, right = start + 1, end

    while left <= right: # 피벗보다 큰 모든 값 찾을 때까지 반복
        while left <= end and array[left] < array[pivot]: # 피벗의 왼쪽파티션에서 피벗보다 큰 데이터 찾기 전까지 +1
            left += 1
        while right >= start and array[right] > array[pivot]: # 피벗의 오른쪽파티션에서 피벗보다 작은 데이터 찾기 전까지 -1
            right -=1

        if left <= right:
            array[right], array[left] = array[left], array[right]
            left += 1
            right -= 1

    array[pivot], array[right] = array[right], array[pivot]

    quicksort(array, start, right-1)
    quicksort(array, right+1, end)
