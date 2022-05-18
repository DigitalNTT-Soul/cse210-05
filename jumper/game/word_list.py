# copy of my test-script for pulling words from the text file,
# we can build the constructor of the class off of this.
f = open("unprocessed word list.txt", 'r')
tab = []

for x in f:
    tab.append(x.strip())

print(tab)
print(len(tab))
f.close()