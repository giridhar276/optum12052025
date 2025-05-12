





# will display all the list of builtin exceptions and functions
print(dir(__builtins__)) 


print(list(range(1,40)))
print(list(range(1,40,2)))

#print(help(range))

val = 10
print(id(val))

alist =[10,430,40]
print(max(alist))
print(min(alist))
print(sum(alist))

#validate alist is list or not
print(isinstance(alist,list))  # True
print(isinstance(alist,dict))  #False
print(isinstance(alist,str))   #Falose

alist = [40,50,6]
atup = tuple(alist)   # tyepcasting - converting from one object to another object


# reading input from keyboard
name = input("Enter your name :")
print(name)