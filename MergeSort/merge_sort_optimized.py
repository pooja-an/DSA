def merge_sort(arr):

    if len(arr) <= 1:
        return

    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_sorted_list(left, right, arr)

def merge_sorted_list(a, b, array):

    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a  and j < len_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
            k += 1
        else:
            array[k] = b[j]
            j += 1
            k += 1

    while i < len_a:
        array[k] = a[i]
        i += 1
        k += 1
            
    while j < len_b:
        array[k] = b[j]
        j += 1
        k += 1


arr = [10,3,15,7,8,23,98,29]
print(arr)
merge_sort(arr)
print(arr)


    
