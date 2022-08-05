a=int(input("enter rows:"))
b=int(input("enter coloum:"))

list=[]
print("enter the rowwise:")

for i in range(0,a):
    x=[]
    for j in range(0,b):
        x.append(int(input()))
    list.append(x)

for i in range(0,a):
    for j in range(0,b):
        print(list[i][j],end="")
    print()


