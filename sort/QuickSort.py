
def quickSort(array, start, end):
    left = start
    right = end
    if left >= right:
        return array
    key = array[left]
    while left < right:
        while left < right and array[right] >= key:
            right = right-1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left = left+1
        array[right] = array[left]
    array[left] = key
    quickSort(array, start, left-1)
    quickSort(array, right+1, end)
    return array
