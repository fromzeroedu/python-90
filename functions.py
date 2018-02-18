def my_function(number_1, number_2, number_3=None):
    if number_3 is not None:
        return ((number_1 + number_2 + number_3)/3)
    else:
        return (number_1 + number_2)

print(my_function(2, 3))
print('---')
print(my_function(2, 3, 4))
print('---')
