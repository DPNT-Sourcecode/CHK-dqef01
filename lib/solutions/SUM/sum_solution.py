# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    
    if type(x) is int and type(y) is int:
        if x <= 0 or y <= 0:
            print('Variable should be greater than 0')    

        return x + y
    else:
        print('Variable should be integer')    
     
print(compute('A',2))