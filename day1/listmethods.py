alist = [10,45,3,56,3,5,435,12]

alist.append(45)
print("After appending:",alist)

alist.extend([67,3,62,73])
print("After exending :",alist)

alist.insert(1,100)
print("After inserting :",alist)

if 1000 in alist:
    alist.remove(1000)
    print("After removing:",alist)
else:
    print("Element not found")


alist.pop(0)  # value at index 0 will be removed
print("AFter pop operation :",alist)


alist.reverse()
print("AFter reversing:",alist)

alist.sort()
print("After sorting:",alist)
alist.sort(reverse=True)
print("After sorting :", alist)