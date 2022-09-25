def InsertionSort(elements):
    for i in range(0, len(elements)):
        for j in range(i+1, len(elements)):
            for k in range(0,j):
                if elements[j] < elements[k]:
                       temp = elements[k]
                       elements[k] = elements[j]
                       elements[j] = temp

nums = [5,4,3,2,1]
print(nums)
InsertionSort(nums)
print(nums)

# Output
'''
[5,4,3,2,1]
[1,2,3,4,5]
'''
                    
            
    
