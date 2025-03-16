
def my_function(*items, **kwargs):
    print(kwargs)
    for value in items:
        print(value)

# my_function('hello', 1, 2, 3, [1, 2, 3], 2, key_one='a', key_two='b')

def function(a, b):
    print(a)
    print(b)

my_list = [1, 'a', 'b', 6]
# my_function(*my_list)
# function(1, 2)
# my_list_two = [1, 2]
# my_list_two.reverse()
# function(*my_list_two)


my_dict = {'a': 3, 'b': 4}

function(**my_dict)
# print('hello', 1, 2, 3, [1, 2, 3])
