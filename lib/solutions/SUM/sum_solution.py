# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if not type(x) is int or not type(y) is int:
        print('Variable should be integer')    

    if x <= 0 or y <= 0:
        print('Variable should be greater than 0')    
     
    return x + y
     
compute(1,2)
