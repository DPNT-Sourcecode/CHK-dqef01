

# noinspection PyUnusedLocal
# skus = unicode string
def Product():
    def __init__(self, description, price):
        self.description = description
        self.price = price
        
def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

print(checkout('AAABCD'))

