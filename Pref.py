file = open("pref.csv")
stuff=[]
for i in file:
    print(i)
    stuff.append(i.split(','))
print (stuff)