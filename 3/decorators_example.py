import random

def generate_random_numbers():
    next_number = 1
    while True:
        next_number = yield random.randint(1, 10) * next_number
        print(next_number)


number_gen = generate_random_numbers()
print(next(number_gen))
print(number_gen.send(10))
print(number_gen.send(10))
print(number_gen.send(10))
print(number_gen.send(10))

