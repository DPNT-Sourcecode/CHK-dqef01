# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    # if type(x) is not int or type(y) is not int:
    #     print('Variable should be integer')    
    print(type(x))
    if x <= 0 or y <= 0:
        print('Variable should be greater than 0')    
     
    return x + y
     
# compute(1,2)
compute('A',2)
