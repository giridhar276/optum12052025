


# using csv library
import csv

try:
    fobj =  open("languages.txt") 
except TypeError as err:
    print("Invalid operation")
except ValueError as err:
    print("Invalid input")
except (IndexError,KeyError) as err:
    print("Invalid index or key.. pl check")
except FileNotFoundError as err:
    print("file is not found")
except Exception as err:
    print(err)
else:
    reader = csv.reader(fobj) # convert file object to csv object
    for line in reader:
        print(line)
finally:
    fobj.close()