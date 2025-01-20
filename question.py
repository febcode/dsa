d = [[1,10],[2,40],[3,90],[4,70],[5,90]]
list = sorted(d,key = lambda i :i[1])
print(list) 

fruits = ['apple','banana','cherry','kiwi']
newlist = [x for x in fruits if 'a' in x]
print(newlist)

import array as arr 
# myArray = arr.array(1,[1,2,3,4,5])
myArray = [1,2,3,4,5]
myArray = myArray[::-1]
print(myArray)


from random import shuffle
k = ['ahana','ponyo','dhanvi','raksha']
print(shuffle(k))

import re
str = 'one-two+three#four'
res = re.split('[-+#]',str)
print(res)

n =5
arr = [0]*n
print(arr)

r = 5 
c = 5 
arr1 = [[0]*c]*r
print(arr1)

arr2 = [[0 for i in range(c)] for j in range(r)]
print(arr2)

dict = {x:x*x for x in range(10)}
print(dict)