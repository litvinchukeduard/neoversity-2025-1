
# 4! = 4 * 3 * 2 * 1
# 0! = 1
def recursive_function(n: int):
    if n <= 0:
        return 1
    
    return n * recursive_function(n - 1)

# print(recursive_function(3))

from pathlib import Path

p = Path('./2')

# [x for x in p.iterdir() if x.is_dir()]
for x in p.iterdir():
    # print(x)
    if x.is_dir():
        print('Folder', x)
    else:
        print('File', x)
