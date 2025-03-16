
'''
Human(children)
'''

# (2, 3) -> 2 * 2 * 2 -> 2 * (2, 2) -> 2 * 2 * 2

def power(number, p):
    # Коли рекурсія зупиняється
    if p == 0:
        return 1

    # Коли рекурсія продовжується
    return number * power(number, p - 1)


def power_tail(number, p, accum=1):
    if p == 0:
        return accum
    
    return power_tail(number, p - 1, accum * number)

def power_loop(number, p):
    accum = 1
    while p > 0:
        accum *= number
        p -= 1
    return accum

print(power_loop(2, 3000))

