n=int(input("enter="))
l=[]
i=n
while n>0:
    rem=n%2
    l.append(rem)
    print(rem)
    n=n//2

l.reverse()
print(l)
