# Creating a list

mylist = ["red" , "black" , "orange"]
print(mylist)

# List allows duplicates

mylist = ["red" , "black" , "orange" , "red"]
print(mylist)

# List length

mylist = ["red" , "black" , "orange"]
print(len(mylist))

# List can be any of the data types

# example 1
mylist = ["red" , 1 , None , 8.575 , True]
print(mylist)

#example 2
mylist1 = ["red" , "black" , "orange"]
mylist2 = [1, 2, 3]
mylist = [3.98, 5.354, 9.617]


# Check type of list

mylist = ["red" , 1 , None , 8.575 , True]
print(type(mylist))


# List constructor

mylist = list(("red" , 1 , None , 8.575 , True))
print(mylist)


# Acecess list items by indexing

# 1. Positive indexing

mylist = ["red" , 1 , None , 8.575 , True]
print(mylist[1])


# 2. Negative indexing

mylist = ["red" , 1 , None , 8.575 , True]
print(mylist[-1])


# 3. Range of indexing 

mylist = ["red" , 1 , None , 8.575 , True]
print(mylist[1:3])

mylist = ["red" , 1 , None , 8.575 , True]
print(mylist[-1:-3])

mylist = ["red" , 1 , None , 8.575 , True]
print(mylist[:3]) # returns the item from beginning to 2nd index

mylist = ["red" , 1 , None , 8.575 , True]
print(mylist[2:]) # returns value from 2nd index to last item it the list


# Check if item exists

mylist = ["red" , 1 , None , 8.575 , True]
if "red" in mylist:
    print("yes red is present in the list")


# Change list items by index

mylist = ["red" , 1 , None , 8.575 , True]
mylist[1] = "green"
print(mylist)    


# Change range of list items by index

mylist = ["red" , 1 , None , 8.575 , True]
mylist[1:2] = "green"
print(mylist)


# Change range of list items by index

mylist = ["red" , 1 , None , 8.575 , True]
mylist[1:3] = ["green" , "yellow"]
print(mylist)


# Insert items

mylist = ["red" , "black" , "orange"]
mylist.insert(1, "green")
print(mylist)


# Add items using append()

mylist = ["red" , "black" , "orange"]
mylist.append("green")
print(mylist)


# Add items using extend()

mylist = ["red" , "black" , "orange"]
mylist2 = ["green" , "yellow"]

mylist.extend(mylist2)
print(mylist)


# Remove item using remove()

mylist = ["red" , "black" , "orange"]
mylist.remove("black")
print(mylist)


# Remove item using pop()

mylist = ["red" , "black" , "orange"]
mylist.pop(1)
print(mylist)


# Remove last item using pop()

mylist = ["red" , "black" , "orange"]
mylist.pop()
print(mylist)


# Remove item using del

mylist = ["red" , "black" , "orange"]
del mylist[1]
print(mylist)


# Delete complete list

mylist = ["red" , "black" , "orange"]
del mylist


# Clear list

mylist = ["red" , "black" , "orange"]
mylist.clear()
print(mylist)


# Loop through a list

mylist = ["red" , "black" , "orange"]

for x in mylist:
    print(x)


# Loop through list using range()

mylist = ["red" , "black" , "orange"]

for i in range(len(mylist)):
    print(mylist[i])


# Loop through list using while loop

mylist = ["red" , "black" , "orange"]

i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1


# List comprehension

mylist = ["red" , "black" , "orange"]

[print(x) for x in mylist]


# Create a new list using list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Sort list in ascending order

numbers = [50, 20, 10, 40, 30]

numbers.sort()

print(numbers)


# Sort list in descending order

numbers = [50, 20, 10, 40, 30]

numbers.sort(reverse=True)

print(numbers)


# Sort string list alphabetically

mylist = ["banana", "apple", "cherry"]

mylist.sort()

print(mylist)


# Reverse a list

mylist = ["red" , "black" , "orange"]

mylist.reverse()

print(mylist)


# Copy a list using copy()

mylist = ["red" , "black" , "orange"]

newlist = mylist.copy()

print(newlist)


# Copy a list using list()

mylist = ["red" , "black" , "orange"]

newlist = list(mylist)

print(newlist)


# Join two lists using +

list1 = ["red" , "black"]
list2 = ["green" , "yellow"]

list3 = list1 + list2

print(list3)


# Join two lists using extend()

list1 = ["red" , "black"]
list2 = ["green" , "yellow"]

list1.extend(list2)

print(list1)


# Count occurrences of an item

mylist = ["red", "black", "red", "orange"]

print(mylist.count("red"))


# Find index of an item

mylist = ["red", "black", "orange"]

print(mylist.index("black"))