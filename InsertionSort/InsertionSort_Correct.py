def InsertionSort(a):
    for i in range(len(a)):
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp

            j = j - 1

                
a = [5,2,3,4,1]
print("Before Sorting: ", a)
InsertionSort(a)
print("After Sorting: ", a)
