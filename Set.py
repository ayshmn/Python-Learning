# Creating a set

myset = {"red", "black", "orange"}
print(myset)


# Set does not allow duplicates

myset = {"red", "black", "orange", "red"}
print(myset)


# Set length

myset = {"red", "black", "orange"}
print(len(myset))


# Set can be any of the data types

# example 1
myset = {"red", 1, None, 8.575, True}
print(myset)

# example 2
myset1 = {"red", "black", "orange"}
myset2 = {1, 2, 3}
myset3 = {3.98, 5.354, 9.617}


# Check type of set

myset = {"red", "black", "orange"}
print(type(myset))


# Set constructor

myset = set(("red", "black", "orange"))
print(myset)


# Access set items

myset = {"red", "black", "orange"}

for x in myset:
    print(x)


# Check if item exists

myset = {"red", "black", "orange"}

if "red" in myset:
    print("yes red is present in the set")


# Add item using add()

myset = {"red", "black", "orange"}

myset.add("green")

print(myset)


# Add multiple items using update()

myset = {"red", "black", "orange"}

myset.update(["green", "yellow"])

print(myset)


# Join two sets using update()

set1 = {"red", "black"}
set2 = {"green", "yellow"}

set1.update(set2)

print(set1)


# Remove item using remove()

myset = {"red", "black", "orange"}

myset.remove("black")

print(myset)


# Remove item using discard()

myset = {"red", "black", "orange"}

myset.discard("black")

print(myset)


# Remove random item using pop()

myset = {"red", "black", "orange"}

myset.pop()

print(myset)


# Clear set

myset = {"red", "black", "orange"}

myset.clear()

print(myset)


# Delete set

myset = {"red", "black", "orange"}

del myset


# Loop through a set

myset = {"red", "black", "orange"}

for x in myset:
    print(x)


# Union of two sets

set1 = {"red", "black"}
set2 = {"green", "yellow"}

set3 = set1.union(set2)

print(set3)


# Using | operator for union

set1 = {"red", "black"}
set2 = {"green", "yellow"}

set3 = set1 | set2

print(set3)


# Intersection of two sets

set1 = {"red", "black", "orange"}
set2 = {"black", "green", "yellow"}

set3 = set1.intersection(set2)

print(set3)


# Using & operator for intersection

set1 = {"red", "black", "orange"}
set2 = {"black", "green", "yellow"}

set3 = set1 & set2

print(set3)


# Difference of two sets

set1 = {"red", "black", "orange"}
set2 = {"black", "green", "yellow"}

set3 = set1.difference(set2)

print(set3)


# Using - operator for difference

set1 = {"red", "black", "orange"}
set2 = {"black", "green", "yellow"}

set3 = set1 - set2

print(set3)


# Symmetric difference

set1 = {"red", "black", "orange"}
set2 = {"black", "green", "yellow"}

set3 = set1.symmetric_difference(set2)

print(set3)


# Using ^ operator for symmetric difference

set1 = {"red", "black", "orange"}
set2 = {"black", "green", "yellow"}

set3 = set1 ^ set2

print(set3)


# Copy a set

myset = {"red", "black", "orange"}

newset = myset.copy()

print(newset)


# Check if sets are disjoint

set1 = {"red", "black"}
set2 = {"green", "yellow"}

print(set1.isdisjoint(set2))


# Check subset

set1 = {"red", "black"}
set2 = {"red", "black", "orange"}

print(set1.issubset(set2))


# Check superset

set1 = {"red", "black", "orange"}
set2 = {"red", "black"}

print(set1.issuperset(set2))