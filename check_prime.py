num = 17
if num >1:
    for i in range(2,int(num/2)+1):
        if (num % i)==0:
            print('not prime')
            break
        else:
            print('num is prime')
            break
else:
    print('not prime')
    
            