from contextlib import contextmanager
'''
Написати функцію, яка після виконання логіки буде писати 'Good bye'
'''

def calculate_sum(number_list: list[int]) -> int:
    return sum(number_list)

@contextmanager
def managed_resource(*args, **kwds): 
    try:
        yield calculate_sum(args)
    finally:
        # Code to release resource, e.g.:
        print("Good bye")


with managed_resource(1, 2, 3, 4, 5, 6) as sum:
    print(sum + 10)
    print(sum + 20)

print("Hello, world")
