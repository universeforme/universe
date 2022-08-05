from datetime import*

current_date=datetime.now()
d1=current_date.date()
print("current date",d1)

cy=d1.strftime("%y")
print("current year=",cy)

cm=d1.strftime("%m")
print("current month=",cm)

cd=d1.strftime("%d")
print("current date",cd)

bd=input("enter birth date=")
b=bd.split("/")

yr1=b[1]
print(yr1)

mr1=b[2]
print(mr1)


# yr=int(yr1)

# mr=int(mr1)

print(cy-yr1)
print(cm-mr1)
