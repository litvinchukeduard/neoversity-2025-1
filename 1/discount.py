# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price= price*(1-discount)
#         # discount_price()
#     apply_discount()
#     return price

# print(discount_price(100, 0.1))

# Ctrl l

price = 100
discount = 0.1

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        # global price
        price= price*(1-discount)

    apply_discount()
    return price

print(discount_price(100, 0.1))

