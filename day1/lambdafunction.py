
### singe liner function
# fixed arguments
# 10 calls
# programs performance degrades
def display(a,b):
    c = a + b
    return c
output = display(10,20)
print(output)


### lambda function
# Execution is faster using lambda function
# lambda is the replacement of singler liner function
#syntax:   functioname = lambda variables: expression
#example: 

display = lambda a,b: a + b
output = display(10,20)
print(output)



# 3. Find maximum of two numbers
maximum = lambda x, y: x if x > y else y
print(maximum(10, 20))  # 20


# 6. Return "Positive" or "Negative"
pos_neg = lambda x: "Positive" if x >= 0 else "Negative"
print(pos_neg(-5))  # Negative

# 7. Square a number
square = lambda x: x ** 2
print(square(6))  # 36



# 9. Get first character of a string
first_char = lambda s: s[0]
print(first_char("Python"))  # P



# 10. Combine two strings
combine = lambda s1, s2: s1 + " " + s2
print(combine("Good", "Morning"))  # Good Morning



############################################################################

nums = [1, 2, 3, 4, 5]

#Output: [1,4,9,16,25]
blist = []
for val in nums:
    blist.append(val ** 2)
print(blist)


#map(function,iterable)
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, nums)))


# 15. Convert list of numbers to their string form
numbers = [10, 20, 30]
as_strings = list(map(lambda x: str(x), numbers))
print(as_strings)  # ['10', '20', '30']