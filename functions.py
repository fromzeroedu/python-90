def my_function(first_name, last_name, address=None, phone=None):
    customer_data = f'{first_name} {last_name}'
    if address is not None:
        customer_data += f', a:{address}'
    if phone is not None:
        customer_data += f', p:{phone}'
    return customer_data

print(my_function('John', 'Jones'))
print('---')
print(my_function('Jane', 'Jones', '12 Main Street'))
print('---')
print(my_function('Julia', 'Jones', '80 Elm Street', '455-322-2222'))
print('---')
print(my_function('Robert', 'Jones', phone='881-555-2455', address='65 Oak Street'))
