

# noinspection PyUnusedLocal
# skus = unicode string

class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price

product_A = Product('A', 50)
print(product_A.price)

def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

print(checkout('AAABCD'))


