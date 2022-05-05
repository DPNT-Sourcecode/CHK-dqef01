

# noinspection PyUnusedLocal
# skus = unicode string

class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price

class Offer:
    def __init__(self, description, price, qtt):
        self.description = description
        self.price = price
        self.qtt = qtt

product_A = {"description": "A",
             "price": 50}
product_B = {"description": "B",
             "price": 30}   
product_C = {"description": "C",
             "price": 20}  
product_D = {"description": "D",
             "price": 15}

products = list()
products.append(product_A)
products.append(product_B)
products.append(product_C)
products.append(product_D)

offer_1 = {"description": "A",
           "qtt": 3,
           "price": 130}   
offer_2 = {"description": "B",
           "qtt": 2,
           "price": 45}  

offers = list()
offers.append(offer_1)
offers.append(offer_2)
#Product('A', 50)
a = Product(**product_A)
b = Product(**product_B)
c = Product(**product_C)
d = Product(**product_D)

o_1 = Offer(**offer_1)
o_2 = Offer(**offer_2)

print(a.price)
print(o_2.qtt)

def calc_offer(sku):



def checkout(skus):
    for item in skus:
        print(item)
    # raise NotImplementedError()

print(checkout('AAABCD'))


