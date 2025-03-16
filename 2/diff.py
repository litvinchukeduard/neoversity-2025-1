import sys
from itertools import zip_longest

from colorama import Fore, Back, Style
# print(Fore.BLUE + 'some red text')
# print(Back.YELLOW + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# print(Fore.BLUE + Back.YELLOW + 'some red text' + Style.RESET_ALL)
# print("Hello")
if len(sys.argv) != 3:
    print("Error: Please enter file path")
    sys.exit(1)

file_one_path = sys.argv[1]
file_two_path = sys.argv[2]

file_one_lines = []
file_two_lines = []

with open(file_one_path) as file_one:
    file_one_lines = file_one.readlines()

with open(file_two_path) as file_two:
    file_two_lines = file_two.readlines()

for file_one_line, file_two_line in zip_longest(file_one_lines, file_two_lines, fillvalue='-'):
    # file_one_line = pair[0]
    # file_two_line = pair[1]
    file_one_line = file_one_line.strip()
    file_two_line = file_two_line.strip()
    if file_one_line != file_two_line:
        print(Fore.RED + file_one_line + Style.RESET_ALL)
        print(Fore.GREEN + file_two_line + Style.RESET_ALL)

    
    

# print(file_one_lines, file_two_lines)
# for item in zip([1, 2, 3, 4], ['sugar', 'spice', 'everything nice', 'hello'], ['a', 'b', 'c']):
#     print(item)

# for item in zip_longest([1, 2, 3, 4], ['sugar', 'spice', 'everything nice', 'hello'], ['a', 'b', 'c'], fillvalue='empty'):
#     print(item)

