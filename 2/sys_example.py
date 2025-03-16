import sys
# import import_example
from import_example import print_hello, pi
'''
Написати додаток, який буде читати усе у файлі
'''
# print(sys.argv)
# print_hello()
# print(pi)

if len(sys.argv) != 2:
    print("Error: Please enter file path")
    sys.exit(1)
    # raise ValueError("Error: Please enter file path")

# print("Working on file...")
# file = open('file.txt')
# file = open(sys.argv[1])
# file.close()
with open(sys.argv[1], encoding='utf-8') as file:
    for line in file:
        print(line.strip())

# input("Eneter number")

