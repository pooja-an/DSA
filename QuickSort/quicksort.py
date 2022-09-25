# implementation of quick sort in python using hoare partition scheme

def swap(i, j, array):
    if i != j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
            
        while end > -1 and elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)
        
    swap(pivot_index, end, elements)
    
    return end
    

def quicksort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quicksort(elements, start, pi-1)
        quicksort(elements, pi+1, end)

a = [11, 9, 29, 7, 2, 15, 28]
print('Before Sorting: ', a)
quicksort(a, 0 , len(a)-1)
print('After Sorting: ', a)


