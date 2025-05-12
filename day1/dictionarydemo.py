book = {"chap1":10 ,"chap2":20,"chap3":30}

print(book)
print(book["chap1"]) #10

if "chap4" in book:   # validating
    print(book["chap4"])
else:
    print("key is not found")

print(book.keys())

# dsiplaying all the keys line by line
for key in book.keys():
    print(key)

## display values
print(book.values())

for value in book.values():
    print(value)

# display key and value
print(book.items())

for k,v in book.items():
    print("key:", k)
    print("Value:",v)

alist = [10,20]
blist = [30,40]
finalist = [alist,blist]   # [[10,20] ,[30,40]]
output = alist + blist    # [10,20,30,40]


## combining dictionaries
newbook = {"chap8":80,"chap9":90}
finalbook = { **book, **newbook}
print(finalbook)

# updating existing book
book.update(newbook)
print(book)