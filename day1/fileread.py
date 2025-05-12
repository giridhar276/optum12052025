# reading the file line by line
with open("languages.txt") as fobj:
    for line in fobj:
        print(line.strip())

# reading to the list
with open("languages.txt","r") as fobj:
    print(fobj.readlines())

# reading to the string
with open("languages.txt") as fobj:
    print(fobj.read())

# using csv library
import csv
with open("languages.txt") as fobj:
    reader = csv.reader(fobj) # convert file object to csv object
    for line in reader:
        print(line)

# using pandas
import pandas as pd
df = pd.read_csv("languages.txt")
print(df)