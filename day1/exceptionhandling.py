


# using csv library
import csv

try:
    with open("languages.txt") as fobj:
        reader = csv.reader(fobj) # convert file object to csv object
        for line in reader:
            print(line)
except Exception as err:
    print(err)
    print("error :", "file is not found..")