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

thistlist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["strawberry", "grape", "watermelon"]
list2 = [1, 5, 7, 9, 3] 
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)


mylist = ["apple", "Banana", "Cherry"]
print(type(mylist))

#It is also possible to use the list() constructor when creating a new list.
thislist = list(("pineapple", "Orange", "Avocado"))
print(thislist)


thislist = ["pineapple", "orange", "avocado"]
print(thislist[1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


thislist = ["orange", "kiwi", "melon", "mango", "Dragon fruit"]
print(thislist[:4])
#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT 


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,


thislist = ["cherry", "orange", "kiwi"]
if "orange" in thislist:
    print("Yes, 'orange' is in the fruit list.")
else:
    print("No!")
    

#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)


list = ["apel", "pisang", "manggis"]
list.insert(2, "semangka")
print(list)


listmakanan = ["indomie", "ramen", "snack"]
listmakanan.append("jeruk")
print(listmakanan)


listbuah = ["kedondong", "leci", "rambutan"]
listmakanan1 = ["chicken", "steak", "frenchfries"]

listbuah.extend(listmakanan1)
print(listbuah)


listmakanan2 = ["KFC", "A&W", "McDonald's"]
listmakanan2.remove("McDonald's")
print(listmakanan2)

#The pop() method removes the specified index.
listmakanan2 = ["KFC", "A&W", "McDonald's"]
listmakanan2.pop(1)
print(listmakanan2)
#OR
#The del keyword also removes the specified index:
listmakanan2 = ["KFC", "A&W", "McDonald's"]
del listmakanan2[0]
print(listmakanan2)

#The clear() method empties the list.
#The list still remains, but it has no content.
listmakanan2 = ["KFC", "A&W", "McDonald's"]
listmakanan2.clear()
print(listmakanan2)

#Python list, Loop Lists
listminuman = ["Jus Alpukat", "Jus Jeruk", "Es Teh"]
for x in listminuman:
    print(x)

#You can also loop through the list items by referring to their index number.
listminuman2 = ["Nu Green Tea", "Aqua", "Pocari Sweat"]
for i in range(len(listminuman2)):
    print(listminuman2[i])

#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
#Remember to increase the index by 1 after each iteration.
makanan = ["Mie Pangsit", "Mie Ayam", "Ayam Goreng Ismail"]
i = 1
while i < len(makanan):
    print(makanan)
    i = i + 1
#SEDIKIT MEMBINGUNGKAN


makanan = ["Mie Pangsit", "Mie Ayam", "Ayam Goreng Ismail"]
[print(y) for y in makanan]


#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

#Complicated Code
fruits = ["Durian", "Kelengkeng", "Pepaya"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#Simple Code
fruits = ["Kiwi", "Leci", "Sirsak", "Mangga", "pisang"]
newlist = [x for x in fruits if "i" in x]

print(newlist)


#With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)


fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits1]

print(newlist)

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits2]

print(newlist)


fruits3 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist= [x if x != "apple" else "durian" for x in fruits3]

print(newlist)


#Python list, Sort List
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
listbuah3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
listbuah3.sort()

print(listbuah3)


listangka = [100, 50, 200, 52, 20,65]
listangka.sort()

print(listangka)


listbuah4 = ["orange", "mango", "kiwi", "pineapple", "banana"]
listbuah4.sort(reverse = True)

print(listbuah4)


listangka1 = [100, 50, 200, 52, 20,65]
listangka1.sort(reverse = True)

print(listangka1)


def myfunc(n):
    return abs(n - 5)

listangka2 = [200, 29, 60, 38, 49]
listangka2.sort(key = myfunc)

print(listangka2)


#Case Insensitive Sort By default the sort() method is case sensitive, 
#resulting in all capital letters being sorted before lower case letters:
listbuah5 = ["banana", "Orange", "Kiwi", "cherry"]
listbuah5.sort()

print(listbuah5)


listbuah5 = ["banana", "Orange", "Kiwi", "cherry"]
listbuah5.sort(key = str.lower)

print(listbuah5)


listbuah6 = ["banana", "Orange", "Kiwi", "cherry"]
listbuah6.reverse()

print(listbuah6)


#make a copy of a list with the copy() method :
listbuah6 = ["apple", "banana", "cherry"]
mylist1 = listbuah6.copy()

print(mylist1)


list4 = ["a", "b", "c"]
list5 = [1, 2, 3]

list6 = list4 + list5

print(list6)


listhuruf = ["d", "e", "f"]
listangka3 = [4, 5, 6]

for x in listhuruf:
    listangka3.append(x)

print(listangka3)
#OR
listhuruf = ["g", "h", "i"]
listangka3 = [7, 8, 9]
listangka3.extend(listhuruf)

print(listangka3)


thistuple = ("apple", "banana", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry", "orange")
print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item, 
#otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Tuple items can be of any data type:
tuple1 = ("banana", "durian", "cherry")
tuple2 = (10, 11, 12, 13)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


tuple4 = ("abc", 24, True, 50, "male")
print(tuple4)


#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "cherry", "banana")
print(thistuple[1])
#Negative Indexing
thistuple = ("apple", "cherry", "banana")
print(thistuple[-1])
#OR
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[3:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-2])

#Python tuples, Access Tuples
