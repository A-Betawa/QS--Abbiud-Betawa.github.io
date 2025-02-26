#print ("Hello, world!")
#if 5>2:
    #print("Five is greater than two!")
    # This is a comment.
    #print ("Hello, World!")
    #print("Hello, World!")
    #print ("Cheers, Mate!")
"""
This is a Comment
written in
more than one line
"""
#print ("Cheers, Mate!")
#x=5
#y="John"
#print(x)
#print(y)
#x=4        # x is of type int
#x="Abbiud" # x is now of type str
#print(x)
#x = str(3)   # x will be '3'
#y = int(3)   # y will be 3
#z = float(3) # z will be 3.0
#print(x , y , z)
#x=5
#y="John"
#print(type(x))
#print(type(y))
#x,y,z = "Oranges", "Banana", "Cherry"
#print(x)
#print(y)
#print(z)
#x=y=z = "Oranges"
#print(x)
#print(y)
#print(z)
#Fruit = ["Apple", "Banana", "Cherry"]
#x,y,z = Fruit
#print(x)
#print(y)
#print(z)
x="Python"
y=" is "
z=" awesome."
#print(x+y+z)
x=5
y=10
#print(x+y)
x=5
y="John"
#print(x,y)

x =" awesome"
def myfunc():
    print("python is" + x)
#myfunc()

x="awesome"
def myfunc():
    global x
    x="fantastic"
myfunc()
#print("python is "+ x)

extra_info = {"hobby": "Biking", "skills": ["Estimating", "BoQ", "Costing"]}
my_dict=(extra_info)
#print(my_dict)

x = 1   #int
y = 2.8 #float
z = 1j  #complex
 #convert from it to float
#a=float(x)
#b=int(y)
#C=complex(x)
#print(a)
#print(b)
#print(C)

import random
#print(random.randrange(1, 10))

#multiline strings
a = """ A QUANTITY SURVEYOR, experienced in Boq and Site management, Precision in using softwares."""
#print(a)

#strings are arrays; use []
a = "Hello, World!"
#print(a[0])

#Looping through a string.
#for x in 'banana':
    #print(x)

#string length
a = 'Hello, World!'
#print(len(a))

#check string.
txt = "The best things in life are free!"
#print('free' in txt)

#using it in an 'if' statement
txt = 'The best things in life are free!'
#if 'free' in txt:
    #print("Yes, 'free' is present.")

txt = 'The best things in life are free!'
#print("Expensive" not in txt)

txt = 'The best things in life are free!'
#if 'expensive' not in txt:
    #print("No, 'expensive' is NOT present.")

#Slicing strings.
b = "Hello, World!"
#print(b[2:5])

#Start index missing (start from the first character).
b = "Hello, World!"
#print(b[:9])

#End index missing (start from the first character).
b = "Hello, World!"
#print(b[2:])

#Negative indexing.
b = "Hello, World!"
#print(b[-5:-2])

#Modify string (uppercase)
b = "Hello, World!"
#print(b.upper())

#Modify string (lowercase)
b = "Hello, World!"
#print(b.lower())

#Modify string (remove whitespace)
b = "Hello, World!"
#print(b.strip())

#Modify string (replacing strings)
b = "Hello, World!"
#print(b.replace("H", "J"))

#Modify string (split string(substrings))
b = "Hello, World!"
#print(b.split(","))

#String combition/combine.
a = "Hello"
b = "World"
c = a + b
#print(c)

#String combition/combine.
a = "Hello"
b = "World"
c = a +" "+ b
#print(c)

#for x in "Banana":
    #print(x)

#'F' Strings as placeholders and modifiers.
Previous_Age = 25 
Current_Age = 3
txt = f"My name is Abbiud and I am {Previous_Age + Current_Age}"
#print(txt)

#.2f fixed point number with 2 decimals (Modifier).
Price = 50
txt = f"The price is {Price: .2f}$"
#print(txt)

# f string with math operation.
txt = f"The price is {20*50}$"
#print(txt)

#Using escape characters(\)
txt = "I am  \"a Quantity Surveyor\" from Nairobi."
#print(txt)

#Booleans.
a = 200
b = 33
#if b>a:
    #print("b is greater than a")
#else:
    #print("b is not greater than a")

Name = "Abbiud"
Grade = 3.56
#print(bool(Name))
#print(bool(Grade))

class myclass():
    def __len__(self):
      return 0
myobj = myclass()
#print(bool(myobj))

def myfunction():
    return True
#print (myfunction())

#You can execute code based on the Boolean answer of a function.
def myfunction():
    return True
#if myfunction():
    print("Yes!")
#else:
    print("No!")

#object is of a certain data type: isinstance()
x = 200
#print(isinstance(x, int))

#python logical operator 'not'
x = 5
#print(not(x>3 and x<10))

#Accessing list items (second item).
thislist = ["Apple", "mangoes", "tea"]
#print(thislist[1])

#Negative index.
#thislist = ["Apple", "tea", "cherry"]
#print(thislist[-1])

#Range of index
thislist = ["Apple", "tea", "cherry"]
#print(thislist[1:3])

thislist = ["Apple", "tea", "cherry"]
#print(thislist[:2])

thislist = ["Apple", "tea", "cherry"]
#print(thislist[1:])

thislist = ["Apple", "tea", "cherry"]
#print(thislist[-3:-2])

thislist = ["Apple", "tea", "cherry"]
#if "cherry" in thislist:
    #print("Yes, 'apple' is in the fruits list")

fruits = ["Apple", "banana", "cherry"]
fruits[1] = "blackcurrent"
#print(fruits)

#Change a range of item value.
#Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
#Matunda[0] = "blackcurrent"
#print(len(Matunda[:]))
#print(Matunda[1:3])
#if "mango" in Matunda:
    #print("IN STOCK!")
#else:
    #Available_Stock = Matunda
    #print(f"OUT OF STOCK!"{})
#INSERTING LESS ITEMS IN LISTS.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Matunda[1:3] = ["blackcurrent"]
#print(Matunda)

#USING .insert() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Matunda.insert(2, "blackcurrent")
#print(Matunda)

#USING .append() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Matunda.append("blackcurrent")
#print(Matunda)

#EXTENDING LIST .extend() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Vegetables = ["Sukuma", "Kunde", "Apoth"]
Matunda.extend(Vegetables)
#print(Matunda)

#Tuple.extend() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Vegetables = ("Sukuma", "Kunde", "Apoth")
Matunda.extend(Vegetables)
#print(Matunda)

#REMOVING LIST ITEMS .remove() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Matunda.remove("cherry")
#print(Matunda)

Matunda = ["apple", "banana", "cherry", "kiwi","cherry", "mango"]
Matunda.remove("cherry")
#print(Matunda)

#Removing specific index .pop() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Matunda.pop()
#print(Matunda)

# del
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
#del Matunda

#Clear the list .clear() function.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
Matunda.clear()
#print(Matunda)

#LOOP THROUGH A LIST 'for'.
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
#for x in Matunda:
    #print(x)

#Loop through the index number 'for', range(len()):
Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
#for i in range(len(Matunda)):
  #print(Matunda[i])

  # MY FIRST APPLICATION. QS ABBIUD BETAWA
#Xmpl. 1 with errors
#Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
#Matunda[0] = "blackcurrent"
#print(len(Matunda[:]))
#print(Matunda[1:3])
#if "mango" in Matunda:
   # print("IN STOCK!")
#else:
    #Available_Stock = Matunda
    #print(f"OUT OF STOCK!"{})

    #Xmpl. 2 with syntax errors.
#Matunda = ["apple", "banana", "cherry", "kiwi", "mango"]
#Matunda[0] = "blackcurrent"
#Current_Inventory = Matunda[:] = Matunda
#print(Matunda[:])
#print(f"All item in Stock: {len(Matunda)}")

#Selected_Items = Current_Inventory - Matunda[:]

#print(f"Selected Items on Cart: {Selected_Items}")

#if "blackcurrent" in Matunda[:3]:
    #print(f"Purchase of {Matunda[:3]} Ready for Payout!")

#elif Matunda[:3] not in Matunda[1:3]:
    #print("NOT in STOCK!")

#else:
    #Available_Stock = Matunda[1:3]
    #print(Available_Stock)

    #Xmpl. 3 with corrected syntax errors.

Matunda = {
    "apple": 10,
    "banana": 5,
    "cherry": 8,                #point of updating stocks. use dict {} function
    "kiwi": 6,
    "mango": 12
}

Matunda["blackcurrent"] = 10       # Assign a stock quantity.

Selected_Items = {"mango": 8}     # Simulate selected items with required quantity(or use user input)

available = {item: qty for item, qty in Selected_Items.items() if item in Matunda and Matunda[item] >= qty}  # Check if selected items are in stock
not_available = {item: qty for item, qty in Selected_Items.items() if item not in Matunda or Matunda[item] < qty}
not_in_inventory = {item: qty for item, qty in Selected_Items.items() if item not in Matunda}

print(f"OUR PRODUCTS!: {Matunda}")          #All Available Stock.

print(f"Selected Items on Cart: {Selected_Items}")

Current_Inventory = Matunda.copy()             #Current inventory snapshot.

print(f"TOTAL items in Stock: {sum(Matunda.values())}") 

if available:
    print(f"Purchase of {available} is Ready for Payout!")  #Check stock status.
    for item, qty in available.items():
        Matunda[item] -= qty
if not_available:
    print(f"NOT in STOCK: {not_available}")   
if not_in_inventory:
    print(f"Item Not in Inventory: {not_in_inventory}")
    
print(f"Updated Inventory: {Matunda}")  # Print updated inventory

