def bubble_sort(elements, key):
    for i in range(len(elements) - 1 ):
        swapped = False
        for j in range(0, len(elements) - i - 1):
            #print(elements[j][key])
            #print(elements[j+1][key])
            if elements[j][key] > elements [j+1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break
    return elements


elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

print(elements)
bubble_sort(elements, key="transaction_amount")
print(elements)

# Output
'''
[
{'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
{'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
{'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
{'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'}
]

[{'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
{'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
{'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
{'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'}]
'''

print(elements)
bubble_sort(elements, key="name")
print(elements)

# Output
'''
[{'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
 {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
 {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
 {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'}]

[{'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
{'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
{'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
{'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'}]

'''

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
bubble_sort(array,'Last Name')

bubble_sort(array,'First Name')

print(*array,sep='\n')

