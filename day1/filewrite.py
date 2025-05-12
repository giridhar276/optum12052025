
# traditional way #regular way
fobj = open("data.txt","w")
fobj.write("unix\n")
fobj.write("python\n")
fobj.writelines(["c","python","ruby"])

for val in range(1,10):
    fobj.write(str(val) + "\n")
fobj.close()


# context manager
# if any line starts with keyword with ... it is called as context manager
# Advantage: file gets closed automatically
# DB connections, network connections, socket connections, remote connections
with open("data1.txt","w") as fobj:
    fobj.write("unix\n")
    fobj.write("python\n")
    fobj.writelines(["c","python","ruby"])

    for val in range(1,10):
        fobj.write(str(val) + "\n")

