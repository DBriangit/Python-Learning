print("Hellew")

if 5 > 2:
    print("Five is greater than two!")


x = 10
y = "Hello, World"

print(x)
print(y)


#this is a comment in python
print("Hello, World!")


#python variables
x = 15
y = "John"
print(x)
print(y)

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

x = 5
y = "Johan"
print(type(x))
print(type(y))

a = 20
A = "Sally"

print(a)
print(A)

myvar = "Alexander1"
my_var = "Alexander2"
_my_var = "Alexander3"
myVar = "Alexander4"
MYVAR = "Alexander5"
myvar2 = "Alexander6"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)   


x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


fruits = ["apple", "grape", "strawberry"]
x, y, z = fruits

print(x)
print(y)
print(z)


x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "really amazing"
print(x, y, z)  
#OR
x = "Python "
y = "is "
z = "cool"
print(x + y + z)


x = 20
y = 30
print (x + y)


x = 10
y = "alexia"
print (x, y)


x = "beautiful"

def myfunc():
    print("Python is " + x)

myfunc()

x = "fun"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
    global x
    x = "Good"

myfunc()

print("Python is " + x)


#Python Numbers
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(1.8)

#convert from int to complex :
z = complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


import random

print(random.randrange(1, 10))

#Python Strings
#Strings are Arrays
#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])


for x in "Banana":
    print(x)

a = "Hello, World!"
print(len(a))    


txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")

txt = "The best things in life are free!"
print("best" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")


b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World"
print(a.replace("H", "J"))

a = "Hello, World!"
b = a.split(",")
print(b)

a = "Hello"
b = "Guys"
c = a + b 
print(c)
#give space
a = "Hello"
b = "Guys"
c = a + " " + b
print(c)


age = 13
txt = "My name is Brian, and I am {}"
print(txt.format(age))

quantity = 3
itemmo = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemmo, price))


txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#Python Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print (bool(False))
print (bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print (bool({}))


class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True

print(myFunction())

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")


x = 200
print(isinstance(x, int))


#Python Operators
print(15 + 20)


#Python Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
