import array as arr 

a=arr.array('i',[]) 

n=int(input('enter n=')) 
for i in range(n):
    arr.append(int(input()))
for i in range(n): 
    print('a[',i,']=',a[i])
    
pos=int(input('enter position=')) 
value=int(input("enter value=")) 
n=n+1
arr.insert(pos,value)
for i in range(n): 
    print('a[',i,']=',a[i])