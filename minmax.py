#import array as c

#from array import *

# import array as c
#a=c.array('i',[])
# print(a)

import array as c

a=c.array('i',[])
n=int(input("n="))
for i in range(0,5):
    a.append(int(input('n=')))

for i in range(0,5):
    print("a[i]=",a[i])

print(max(a))
print(min(a))

temp=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        
    print('a[{}]='.format(i),a[i])

rem=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            rem=a[i]
            a[i]=a[j]
            a[j]=rem
        
    print('a[{}]='.format(i),a[i])
