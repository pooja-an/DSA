def bubble_sort(elements):
    for i in range(len(elements) - 1 ):
        swapped = False
        for j in range(0, len(elements) - i - 1):
            if elements[j] > elements [j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break
    return elements


nums = [5,4,2,3,1]
print(nums)

nums = bubble_sort(nums)
print(nums)

# Output
# [5, 4, 2, 3, 1]
# [1, 2, 3, 4, 5]

nums = [1,4,8]
print(nums)

nums = bubble_sort(nums)
print(nums)

# Output
# [1,4,8]
# [1,4,8]
