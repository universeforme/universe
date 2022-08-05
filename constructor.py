class demo:

    #class instanc
    #cyrrent class instanc variable
    a=0
    b=0
    c=0
    def __init__(self):
        a=int(input("a="))
        b=int(input("b="))
        c=int(input("c="))
        self.a=a
        self.b=b
        self.c=c

    def get(self):
        print("sum=",self.a+self.b+self.c)

    def don(self):
        print("per=",(self.a+self.b+self.c)/5)

    def min(self):
        x=[self.a,self.b,self.c]
        print(min(x))

    def max(self):
        x=[self.a,self.b,self.c]
        print(max(x))

d=demo()
d.get()
d.don()
d.min()
d.max()
