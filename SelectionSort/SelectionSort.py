def SelectionSort(array):

    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]             

array = [5,4,3,2,1]
print(array)
SelectionSort(array)
print(array)


array = [5,4,3,2,1]
print(array)
selection_sort(array)
print(array)


# Output
'''
[5, 4, 3, 2, 1]
[1, 2, 3, 4, 5]
'''
