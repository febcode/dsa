def bs(a):
    b = len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y],a[y+1] = a[y+1],a[y]
                
    return a 
                
                
                
a = [32,5,3,6,7,54,87]
print(bs(a))