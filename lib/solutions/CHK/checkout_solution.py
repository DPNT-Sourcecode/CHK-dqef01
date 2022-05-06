

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import count

class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price

class Offer:
    def __init__(self, description, price, qtt, get_one_free):
        self.description = description
        self.price = price
        self.qtt = qtt
        self.get_one_free = get_one_free

product_A = {"description": "A",
             "price": 50}
product_B = {"description": "B",
             "price": 30}   
product_C = {"description": "C",
             "price": 20}  
product_D = {"description": "D",
             "price": 15}
product_E = {"description": "E",
             "price": 40}

products = list()
products.append(product_A)
products.append(product_B)
products.append(product_C)
products.append(product_D)
products.append(product_E)

offer_1 = {"description": "A",
           "qtt": 3,
           "price": 130,
           "get_one_free" : ""}   
offer_2 = {"description": "B",
           "qtt": 2,
           "price": 45,
           "get_one_free" : ""}  
offer_3 = {"description": "A",
           "qtt": 5,
           "price": 200,
           "get_one_free": ""}
offer_4 = {"description": "E",
           "qtt": 2,
           "price": 80,
           "get_one_free": "B"}

offers = list()

offers.append(offer_3)
offers.append(offer_1)
offers.append(offer_2)
offers.append(offer_4)

# a = Product(**product_A)
# b = Product(**product_B)
# c = Product(**product_C)
# d = Product(**product_D)

# o_1 = Offer(**offer_1)
# o_2 = Offer(**offer_2)

def calc_product(sku, qtt_product):
    list_offers = list(filter(lambda x: x['description'] == sku, offers))
    list_offers = list(filter(lambda x: x['qtt'] <= qtt_product, list_offers))
    
    list_products = list(filter(lambda x: x['description'] == sku, products))
    product = Product(**list_products[-1])
    
    if list_offers:
        amount = 0
        rest = 0
        for item in list_offers:
            offer = Offer(**item)
            while qtt_product >= offer.qtt:
            
                qtt_offer = int(qtt_product / offer.qtt)
                amount = amount + qtt_offer * offer.price
                rest = (qtt_product - (qtt_offer * offer.qtt))
                qtt_product = qtt_product - offer.qtt
            
        if rest > 0:
            amount = amount + (rest * product.price)

    else:
        amount = product.price * qtt_product

    return amount   

def checkout(skus):
    amount = 0

    if sum(map(str.islower, skus)) > 0:
        return -1
    else:
        for product in products:
            p = Product(**product)
            qtt = skus.count(p.description)
            if qtt > 0:
                product_amount = calc_product(p.description,qtt)
                amount += product_amount
            
                list_offers = list(filter(lambda x: x['description'] == p.description, offers))
            
                if list_offers:
                    offer = Offer(**list_offers[-1])
                    
                    if offer.get_one_free != "":
                        list_products_free = list(filter(lambda x: x['description'] == offer.get_one_free, products))
                        product_for_free = Product(**list_products_free[-1])
                        qtt_for_free = skus.count(offer.get_one_free)

                        if qtt_for_free > 0:
                            amount = amount - product_for_free.price
                        
        if amount > 0 or skus == "":
            return amount
        else:
            return -1
                
print(checkout('AAAAAAAAAA'))                
