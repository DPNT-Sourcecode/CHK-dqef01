

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
# creating group of offers        
class Group_Offer:
    def __init__(self, group, sku):
        self.group = group
        self.sku = sku     
# defining the offer group attribute values as we won't have any database   
group_offer_1 = {"group": "&",
                 "sku": "S"}
group_offer_2 = {"group": "&",
                 "sku": "T"}
group_offer_3 = {"group": "&",
                 "sku": "X"}
group_offer_4 = {"group": "&",
                 "sku": "Y"}
group_offer_5 = {"group": "&",
                 "sku": "Z"}
list_groups = list()
list_groups.append(group_offer_1) 
list_groups.append(group_offer_2)
list_groups.append(group_offer_3)
list_groups.append(group_offer_4)
list_groups.append(group_offer_5)                
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
product_G = {"description": "G",
             "price": 20}
product_H = {"description": "H",
             "price": 10}
product_I = {"description": "I",
             "price": 35}
product_J = {"description": "J",
             "price": 60}
# product_K = {"description": "K",
#              "price": 80}
product_K = {"description": "K",
             "price": 70}
product_L = {"description": "L",
             "price": 90}
product_M = {"description": "M",
             "price": 15}
product_N = {"description": "N",
             "price": 40}
product_O = {"description": "O",
             "price": 10}
product_P = {"description": "P",
             "price": 50}
product_Q = {"description": "Q",
             "price": 30}
product_R = {"description": "R",
             "price": 50}
# product_S = {"description": "S",
#              "price": 30}
product_S = {"description": "S",
             "price": 20}
product_T = {"description": "T",
             "price": 20}
product_U = {"description": "U",
             "price": 40}
product_V = {"description": "V",
             "price": 50}
product_W = {"description": "W",
             "price": 20}
# product_X = {"description": "X",
#              "price": 90}
product_X = {"description": "X",
             "price": 17}             
# product_Y = {"description": "Y",
#              "price": 10}
product_Y = {"description": "Y",
             "price": 20}             
# product_Z = {"description": "Z",
#              "price": 50}
product_Z = {"description": "Z",
             "price": 21}
#creating and insertint a list of products

products = list()
# for x in skus_registered:
products.append(product_A)
products.append(product_B)
products.append(product_C)
products.append(product_D)
products.append(product_E)
products.append(product_F)
products.append(product_G)
products.append(product_H)
products.append(product_I)
products.append(product_J)
products.append(product_K)
products.append(product_L)
products.append(product_M)
products.append(product_N)
products.append(product_O)
products.append(product_P)
products.append(product_Q)
products.append(product_R)
products.append(product_S)
products.append(product_T)
products.append(product_U)
products.append(product_V)
products.append(product_W)
products.append(product_X)
products.append(product_Y)
products.append(product_Z)

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
offer_6 = {"description": "H",
           "qtt": 10,
           "price": 80,
           "product_free": "",
           "product_free_qtt": 0}           
offer_7 = {"description": "H",
           "qtt": 5,
           "price": 45,
           "product_free": "",
           "product_free_qtt": 0}  
offer_8 = {"description": "K",
           "qtt": 2,
           "price": 150,
           "product_free": "",
           "product_free_qtt": 0}  
offer_9 = {"description": "N",
           "qtt": 3,
           "price": 120,
           "product_free": "M",
           "product_free_qtt": 1}  
offer_10 = {"description": "P",
           "qtt": 5,
           "price": 200,
           "product_free": "",
           "product_free_qtt": 0}  
offer_11 = {"description": "Q",
           "qtt": 3,
           "price": 80,
           "product_free": "",
           "product_free_qtt": 0}
offer_12 = {"description": "R",
           "qtt": 3,
           "price": 150,
           "product_free": "Q",
           "product_free_qtt": 1}
offer_13 = {"description": "U",
           "qtt": 4,
           "price": 160,
           "product_free": "U",
           "product_free_qtt": 1}
offer_14 = {"description": "V",
           "qtt": 3,
           "price": 130,
           "product_free": "",
           "product_free_qtt": 0}
offer_15 = {"description": "V",
           "qtt": 2,
           "price": 90,
           "product_free": "",
           "product_free_qtt": 0}
offer_G = {"description": "&",
           "qtt": 3,
           "price": 45,
           "product_free": "",
           "product_free_qtt": 0}           
#creating and insertint a list of offers
offers = list()
offers.append(offer_3)
offers.append(offer_1)
offers.append(offer_2)
offers.append(offer_4)
offers.append(offer_5)
offers.append(offer_6)
offers.append(offer_7)
offers.append(offer_8)
offers.append(offer_9)
offers.append(offer_10)
offers.append(offer_11)
offers.append(offer_12)
offers.append(offer_13)
offers.append(offer_14)
offers.append(offer_15)
# function to calculate the products according to the expected rules
def calc_product(skus, sku, qtt_product):
    # look up the offer
    list_offers = list(filter(lambda x: x['description'] == sku, offers))
    list_offers = list(filter(lambda x: x['qtt'] <= qtt_product, list_offers))
    
    # look up the product and instantiate it
    list_products = list(filter(lambda x: x['description'] == sku, products))
    product = Product(**list_products[-1])
 
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
# calc group of offers    
# def calc_groups(skus):
#     gCount = 0
#     for s in skus:
#         # 'STUV' 'STZ' 'AAASTZ'
#         groups = list(filter(lambda x: x['sku'] == group.sku, list_groups))

#         if groups:
#             g = Group_Offer(**groups[-1])
#             if g.sku:
#                 gCount += 1

#     for item in list_groups:
#         group = Group_Offer(**item)
#         list_offers_g = list(filter(lambda x: x['sku'] == group.sku, offers))


    
            


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
                
print(checkout('QQQQQ'))    
