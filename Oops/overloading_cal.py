from multipledispatch import dispatch

@dispatch(int)
def calci(a):
    res=a*a
    print("square",res)

@dispatch(int,int)
def calci(a,b):
    add=a+b
    print("addition",add)

calci(2)
calci(3,5)