

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import count

# creating product class
class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price
# creating offer class
class Offer:
    def __init__(self, description, price, qtt, product_free, product_free_qtt):
        self.description = description
        self.price = price
        self.qtt = qtt
        self.product_free = product_free
        self.product_free_qtt = product_free_qtt
#defining the product attribute values as we won't have any database
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
product_F = {"description": "F",
             "price": 10}
#creating and insertint a list of products
products = list()
products.append(product_A)
products.append(product_B)
products.append(product_C)
products.append(product_D)
products.append(product_E)
products.append(product_F)
#defining the offer attribute values as we won't have any database
offer_1 = {"description": "A",
           "qtt": 3,
           "price": 130,
           "product_free" : "",
           "product_free_qtt": 0}   
offer_2 = {"description": "B",
           "qtt": 2,
           "price": 45,
           "product_free" : "",
           "product_free_qtt": 0}  
offer_3 = {"description": "A",
           "qtt": 5,
           "price": 200,
           "product_free": "",
           "product_free_qtt": 0}
offer_4 = {"description": "E",
           "qtt": 2,
           "price": 80,
           "product_free": "B",
           "product_free_qtt": 1}
offer_5 = {"description": "F",
           "qtt": 3,
           "price": 30,
           "product_free": "F",
           "product_free_qtt": 1}           
#creating and insertint a list of offers
offers = list()
offers.append(offer_3)
offers.append(offer_1)
offers.append(offer_2)
offers.append(offer_4)
offers.append(offer_5)
# function to calculate the products according to the expected rules
def calc_product(skus, sku, qtt_product):
    # look up the offer
    list_offers = list(filter(lambda x: x['description'] == sku, offers))
    list_offers = list(filter(lambda x: x['qtt'] <= qtt_product, list_offers))
    
    # look up the product and instantiate it
    list_products = list(filter(lambda x: x['description'] == sku, products))
    product = Product(**list_products[-1])

    # # look up extra offers to avoid having duplicated offers
    # list_extra_offer = list(filter(lambda x: x['product_free'] == sku, offers))
    # # verify if description exists in skus
    # qtt_skus_offer = 0
    # if list_extra_offer: 
    #     extra_offer = Offer(**list_extra_offer[-1])
    #     qtt_skus_offer = skus.count(extra_offer.description)
    #     # if skus.count(extra_offer.description) > extra_offer.product_free_qtt:
    #     #     cancel_offer = True
    
    if list_offers:
        amount = 0
        rest = 0
        for item in list_offers:
            offer = Offer(**item)

            while qtt_product >= offer.qtt:
                
                # calc normal offer
                qtt_offer = int(qtt_product / offer.qtt)
                amount = amount + offer.price
                rest = (qtt_product - (qtt_offer * offer.qtt))
                qtt_product = qtt_product - offer.qtt
                
                # calc rule to get products for free
                # if offer.product_free != "" and offer.product_free_qtt > 0:
                #     list_products_free = list(filter(lambda x: x['description'] == offer.product_free, products))
                #     product_for_free = Product(**list_products_free[-1])
                #     qtt_products_free = skus.count(offer.product_free)
                    
                #     if qtt_products_free >= offer.product_free_qtt:
                #         amount = amount - (product_for_free.price * offer.product_free_qtt)
                #         qtt_products_free = qtt_products_free - offer.product_free_qtt
                        
        if rest > 0:
            amount = amount + (rest * product.price)

    else:
        amount = product.price * qtt_product

    return amount   
def remove_skus_free(skus):
    for product in products:
        p = Product(**product)
        # look up extra offers to avoid having duplicated offers
        list_extra_offer = list(filter(lambda x: x['description'] == p.description, offers))
        # verify if description exists in skus
        if list_extra_offer:
            for extra_offer in list_extra_offer:
                offer = Offer(**extra_offer)
                if offer.product_free != "" and offer.product_free_qtt > 0:
                    qtt_skus_offer = skus.count(p.description) 

                    while qtt_skus_offer >= offer.qtt:
                        qtt_skus_offer = qtt_skus_offer - offer.qtt
                        skus = skus.replace(offer.product_free, "", offer.product_free_qtt)
                        
    return skus

# expected checkout function
def checkout(skus):
    skus = remove_skus_free(skus)
    amount = 0
    if sum(map(str.islower, skus)) > 0:
        return -1
    else:
        for product in products:
            p = Product(**product)
            qtt = skus.count(p.description)
            if qtt > 0:
                product_amount = calc_product(skus,p.description,qtt)
                amount += product_amount
                        
        if amount > 0 or skus == "":
            return amount
        else:
            return -1
                
print(checkout('FFFFF'))    
