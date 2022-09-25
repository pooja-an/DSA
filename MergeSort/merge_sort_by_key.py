def merge_sort(arr, key):
    if len(arr) <= 1:
        return

    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left, key)
    merge_sort(right, key)
    
    merge_sorted_list(left, right, arr, key)

def merge_sorted_list(a, b, array, key):

    len_a = len(a)
    len_b = len(b)
    
    i = j = k = 0

    while i < len_a  and j < len_b:
        if a[i][key] <= b[j][key]:
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

elements = [{'name': 'rajab', 'age': 12, 'time_hours': 3},{'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
            {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},{'name': 'vedanth', 'age': 17, 'time_hours': 1}]
print('Before Sorting by name:')
print(*elements, sep='\n')
merge_sort(elements, 'name')
print('After Sorting by name:')
print(*elements, sep='\n')

    
