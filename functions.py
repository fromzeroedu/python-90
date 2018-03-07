no_address = False

def my_function(first_name, last_name, address=None, phone=None):
    global customer_data
    global no_address
    customer_data = f'{first_name} {last_name}'
    if address is not None:
        no_address = False
        customer_data += f', a:{address}'
    else:
        no_address = True
    if phone is not None:
        customer_data += f', p:{phone}'
    return customer_data

print(my_function('John', 'Jones'))
print('no_address', no_address)
print('---')
print(my_function('Jane', 'Jones', '12 Main Street'))
print('no_address', no_address)
print('---')
print(my_function('Julia', 'Jones', '80 Elm Street', '455-322-2222'))
print('---')
print(my_function('Robert', 'Jones', phone='881-555-2455', address='65 Oak Street'))
print('---')
print('customer_data', customer_data)
