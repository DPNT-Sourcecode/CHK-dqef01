

# noinspection PyUnusedLocal
# skus = unicode string

product_A = {"A": 50}
product_B = {"B": 30}
product_C = {"C": 20}
product_D = {"D": 15}

list = []

list.append(product_A)
list.append(product_B)
print(list)

def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

def Product():
    def __init__(self, description, price):
        self.description = description
        self.price = price

print(checkout('AAABCD'))

