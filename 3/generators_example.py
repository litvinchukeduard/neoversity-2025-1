import random

def generate_random_numbers():
    next_number = 1
    while True:
        next_number = yield random.randint(1, next_number)
        print(next_number)


number_gen = generate_random_numbers()
print(next(number_gen))
print(number_gen.send(2))
print(number_gen.send(3))
print(number_gen.send(4))
print(number_gen.send(5))

