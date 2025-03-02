
counter = 0
LOG_FILE = 'hello.txt'

def print_hello():
    global counter
    counter += 1
    print(counter)
    print("Hello")

def print_world():
    global counter
    counter *= 2
    print(counter)
    print("World")


# print_hello()
# print_hello()
# print_world()
# print_hello()
# print_hello()


def print_hello_closure():
    counter = 0

    def printer():
        nonlocal counter
        counter += 1
        print(counter)
        print("hello")
    return printer

print(sum([1, 2, 3]))

my_sum_function = sum

print(my_sum_function([1, 2, 3]))

printer = print_hello_closure()
printer()
printer()
printer()

