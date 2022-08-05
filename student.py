#class demo():

#     def get(self,a):
#         print("hello=",a)

#     def test(self):
#         print("test")

# d=demo()
# d.get(12)
# d.test()

class demo():

    def chinki(self):
        a=int(input("a="))
        b=int(input("b="))
        c=int(input("c="))
        d=int(input("d="))
        e=int(input("e="))

        return a,b,c,d,e

    def get(self,a,b,c,d,e):
        sum=a+b+c+d+e
        print('total of sum=',sum)

        return sum

    def run(self,a,b,c,d,e):
        per=(a+b+c+d+e)/5
        print('per=',per)

    def luck(self):
        x=[a,b,c,d,e]
        print(min(x))

    def bro(self):
        y=[a,b,c,d,e]
        print(max(y))
z=demo()

a,b,c,d,e=z.chinki()
sum=z.get(a,b,c,d,e)
z.run(a,b,c,d,e)

z.luck()
z.bro()

# class demo():

#     def get(self,a,b,c,d,e):
#         sum=a+b+c+d+e
#         print('total of sum=',sum)

#     def run(self,a,b,c,d,e):
#         per=(a+b+c+d+e)/5
#         print('per=',per)

#     def luck(self):
#         x=[a,b,c,d,e]
#         print(min(x))

#     def bro(self):
#         y=[a,b,c,d,e]
#         print(max(y))


# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
# e=int(input("e="))

# z=demo()

# z.get(a,b,c,d,e)
# z.run(a,b,c,d,e)

# z.luck()
# z.bro()