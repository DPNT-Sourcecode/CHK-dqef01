

# noinspection PyUnusedLocal
# skus = unicode string

product_A = {"A": 50}
product_B = {"B": 30}
product_C = {"C": 20}
product_D = {"D": 15}

# list = []

# list.append(product_A)
# list.append(product_B)
# print(list)

def Product():
    def __init__(self, description, price):
        self.description = description
        self.price = price

item1 = Product(product_A)     
print(item1.description)

def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

print(checkout('AAABCD'))