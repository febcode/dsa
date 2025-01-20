nterms = int(input("how many item"))
n1,n2 = 0,1
count = 0

if nterms<0:
    print('enter positive')
elif nterms==1:
    print(n1)
else:
    while count<nterms:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count+1