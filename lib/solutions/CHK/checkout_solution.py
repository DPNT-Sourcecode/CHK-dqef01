

# noinspection PyUnusedLocal
# skus = unicode string

products = {}

def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

def Product():
    def __init__(self, description, price):
        self.description = description
        self.price = price

print(checkout('AAABCD'))
