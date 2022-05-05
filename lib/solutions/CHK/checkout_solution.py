

# noinspection PyUnusedLocal
# skus = unicode string

class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price

product_A = {"description": "A",
             "price": 50}
product_B = {"description": "B",
             "price": 30}   
product_C = {"description": "C",
             "price": 20}  
product_D = {"description": "D",
             "price": 15}
offer_1 = {"description": "A",
           "qtt": 3,
           "price": 130}                                                
#Product('A', 50)
a = Product(**product_A)
print(a.price)

def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

print(checkout('AAABCD'))




