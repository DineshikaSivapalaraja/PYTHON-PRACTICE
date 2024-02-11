#basic data types in python: Numbers,Strings,Booleans, SEqueemces, Dictionary

myint = 6
myfloat = 12.8
mystr = "This is a String"
mybool = True #true--can't
mylist = [0, 1, "two", 3.2, False]
mytuple = (0,1,2)
mydict = {"one": 1, "two": 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)


#redeclare a variable
myint = "din"
print(myint)

#to access a member of a sequence type, use[]
print(mylist[1])
print(mytuple[0])

#use slices to get parts of sequence
print(mylist[1:5])
print(mylist[1:5:2])

#youcan use slices to reverse a sequemce
print(mylist[::-1])

#dictionaries are accessed via key
print(mydict["one"])

#ERROR: variables of different types cannot be combined
print("string type" + str(123))
#print("string type"+ 123)

#Global vs local variables in functions
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

# del mystr
# print(mystr)



