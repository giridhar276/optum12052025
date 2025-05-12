# fixed arguments
def display(a,b):
    c = a + b
    return c
output = display(10,20)
print(output)

# default arguments # function ovrloading
def display(a = 0,b = 0,c = 0):
    print(a,b,c)

display() # 0 0 0 
display(10) # 10 0 0 
display(10,20) # 10 20 0
display(10,20,30)  # 10 20 30

# keyword arguments
def display(b,a,c):
    print(a,b,c)
display(c= 30 , a = 10 , b = 20)

# variable length argumnets
def display(*args):  # *args is the tuple
    print(args)
    for val in args:
        print(val)

display(10,20,30,40,67,3,2,56,32,67,32,67,32,75,3,672,4,56,1)