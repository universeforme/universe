a=10


try:
    a1=a/0
    print(a1)
except:
    print("cannot be divided by 0")
finally:
    print("welcome")