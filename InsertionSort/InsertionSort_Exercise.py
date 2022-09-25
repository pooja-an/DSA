def SelectionSort(array, keys):
    for key in keys[-1::-1]:
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j][key] < array[i][key]:
                    temp = array[j]
                    array[j] = array[i]
                    array[i] = temp
               
array =[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
SelectionSort(array,['First Name','Last Name'])
print(f'Array after Multi-Level Sorting:', *array, sep='\n')

# Output:
'''Array after Multi-Level Sorting:
{'First Name': 'Aahana', 'Last Name': 'Arora'}
{'First Name': 'Armaan', 'Last Name': 'Dadra'}
{'First Name': 'Armaan', 'Last Name': 'Kumar'}
{'First Name': 'Ingrid', 'Last Name': 'Galore'}
{'First Name': 'Ingrid', 'Last Name': 'Maverick'}
{'First Name': 'Jade', 'Last Name': 'Canary'}
{'First Name': 'Jaya', 'Last Name': 'Seth'}
{'First Name': 'Jaya', 'Last Name': 'Sharma'}
{'First Name': 'Karan', 'Last Name': 'Kumar'}
{'First Name': 'Kiran', 'Last Name': 'Kamla'}
{'First Name': 'Raj', 'Last Name': 'Nayyar'}
{'First Name': 'Raj', 'Last Name': 'Sharma'}
{'First Name': 'Raj', 'Last Name': 'Thakur'}
{'First Name': 'Suraj', 'Last Name': 'Sharma'}
'''
