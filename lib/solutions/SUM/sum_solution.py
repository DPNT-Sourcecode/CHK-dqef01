# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x <= 0 or y <= 0:
        print('Variable should be greater than 0')    

    if type(x) is int and type(y) is int:
        return x + y
    else:
        print('Variable should be integer')    
     
# compute(1,2)
compute('A',2)