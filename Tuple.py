# Creating a tuple

mytuple = ("red", "black", "orange")
print(mytuple)


# Tuple allows duplicates

mytuple = ("red", "black", "orange", "red")
print(mytuple)


# Tuple length

mytuple = ("red", "black", "orange")
print(len(mytuple))


# Tuple can be any of the data types

# example 1
mytuple = ("red", 1, None, 8.575, True)
print(mytuple)

# example 2
mytuple1 = ("red", "black", "orange")
mytuple2 = (1, 2, 3)
mytuple3 = (3.98, 5.354, 9.617)


# Check type of tuple

mytuple = ("red", 1, None, 8.575, True)
print(type(mytuple))


# Tuple constructor

mytuple = tuple(("red", 1, None, 8.575, True))
print(mytuple)


# Create tuple with one item

mytuple = ("red",)
print(type(mytuple))


# Access tuple items by indexing

# 1. Positive indexing

mytuple = ("red", 1, None, 8.575, True)
print(mytuple[1])


# 2. Negative indexing

mytuple = ("red", 1, None, 8.575, True)
print(mytuple[-1])


# 3. Range of indexing

mytuple = ("red", 1, None, 8.575, True)
print(mytuple[1:3])

mytuple = ("red", 1, None, 8.575, True)
print(mytuple[:3])

mytuple = ("red", 1, None, 8.575, True)
print(mytuple[2:])


# Check if item exists

mytuple = ("red", 1, None, 8.575, True)

if "red" in mytuple:
    print("yes red is present in the tuple")


# Tuples are unchangeable

mytuple = ("red", "black", "orange")

# Convert tuple into list
temp = list(mytuple)

temp[1] = "green"

# Convert back to tuple
mytuple = tuple(temp)

print(mytuple)


# Add items to tuple

mytuple = ("red", "black", "orange")

temp = list(mytuple)

temp.append("green")

mytuple = tuple(temp)

print(mytuple)


# Remove items from tuple

mytuple = ("red", "black", "orange")

temp = list(mytuple)

temp.remove("black")

mytuple = tuple(temp)

print(mytuple)


# Join two tuples

tuple1 = ("red", "black")
tuple2 = ("green", "yellow")

tuple3 = tuple1 + tuple2

print(tuple3)


# Multiply tuple

mytuple = ("red", "black")

result = mytuple * 2

print(result)


# Loop through a tuple

mytuple = ("red", "black", "orange")

for x in mytuple:
    print(x)


# Loop through tuple using range()

mytuple = ("red", "black", "orange")

for i in range(len(mytuple)):
    print(mytuple[i])


# Loop through tuple using while loop

mytuple = ("red", "black", "orange")

i = 0

while i < len(mytuple):
    print(mytuple[i])
    i += 1


# Count occurrences of an item

mytuple = ("red", "black", "red", "orange")

print(mytuple.count("red"))


# Find index of an item

mytuple = ("red", "black", "orange")

print(mytuple.index("black"))


# Tuple unpacking

mytuple = ("red", "black", "orange")

color1, color2, color3 = mytuple

print(color1)
print(color2)
print(color3)


# Using asterisk in unpacking

mytuple = ("red", "black", "orange", "green")

color1, *color2, color3 = mytuple

print(color1)
print(color2)
print(color3)
