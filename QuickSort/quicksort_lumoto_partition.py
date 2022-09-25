def swap(i, j, array):
    if i != j:
        #print('SWAP->','pi= ',i,' i= ',j,array)        
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

def partition_raw(elements):
    pivot_index = len(elements) -1
    pivot = elements[pivot_index]

    pi = 0
    i = pi + 1

    while pi < len(elements)-1:
        while pi < len(elements)-1 and elements[pi] <= pivot:
            pi += 1

        i = pi + 1

        while i < len(elements) and  elements[i] > pivot:
            i += 1

        swap(pi, i, elements)
        pi += 1
        i += pi

def partition(elements, end):
    #print(elements,'end->', end)
    if end <= 0:
        return
    
    pivot_index = end
    pivot = elements[pivot_index]

    pi = 0
    i = pi + 1

    while pi < end and i < end:
        while pi < end and elements[pi] <= pivot:
            pi += 1

        i = pi + 1

        while i < end and elements[i] > pivot:
            i += 1

        if i < end:
            swap(pi, i, elements)
            pi += 1
            i += pi
        
    if elements[pi] > pivot:
        swap(pi,pivot_index,elements)
        
    partition(elements, end -1)
    


def quicksort(elements):
    partition(elements, len(elements)-1)
    

#a = [11, 9, 29, 7, 2, 15, 28]
#quicksort(a)
#print(a)

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

for elements in tests:
    quicksort(elements)
    print(f'sorted array: {elements}')    
