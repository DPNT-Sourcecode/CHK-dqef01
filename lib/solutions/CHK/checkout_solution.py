

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import count

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
offer_3 = {"description": "A",
           "qtt": 5,
           "price": 200}

offers = list()

offers.append(offer_3)
offers.append(offer_1)
offers.append(offer_2)

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

    amount = 0
    print(list_offers)
    if list_offers:
        print(list_offers)

        for item in list_offers:
            
            offer = Offer(**item)

            qtt_offer = int(qtt_product / offer.qtt)
            amount = qtt_offer * offer.price
            rest = (qtt_product - (qtt_offer * offer.qtt))
            amount = amount + (rest * product.price)

            list_offers = list(filter(lambda x: x['qtt'] <= rest, list_offers))
                
            # more_offers = list(filter(lambda x: x['qtt'] <= rest, list_offers))
            # print(amount)
            
            # if more_offers:
            #     new_offer = Offer(**more_offers[-1])
            #     qtt_new_offer = int(rest / new_offer.qtt)
            #     amount_new = qtt_new_offer * new_offer.price
            #     new_rest = (rest - (qtt_new_offer * new_offer.price))
            #     amount = amount + amount_new + (new_rest * product.price)

            
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
            product_amount = calc_product(p.description,qtt)
            amount += product_amount
        if amount > 0 or skus == "":
            return amount
        else:
            return -1
                
print(checkout('AAAA'))                
