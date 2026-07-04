# Creating a dictionary

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict)


# Dictionary items are ordered

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict)


# Dictionary does not allow duplicate keys

mydict = {
    "color1": "red",
    "color1": "black",
    "color3": "orange"
}
print(mydict)


# Dictionary length

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(len(mydict))


# Dictionary can contain different data types

mydict = {
    "name": "Ayesha",
    "age": 20,
    "is_student": True,
    "percentage": 85.5,
    "city": None
}
print(mydict)


# Check type of dictionary

mydict = {
    "color1": "red",
    "color2": "black"
}
print(type(mydict))


# Dictionary constructor

mydict = dict(
    color1="red",
    color2="black",
    color3="orange"
)
print(mydict)


# Access dictionary items using key

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict["color2"])


# Access items using get()

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict.get("color2"))


# Get all keys

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict.keys())


# Get all values

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict.values())


# Get all items

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}
print(mydict.items())


# Check if key exists

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

if "color1" in mydict:
    print("yes color1 is present in dictionary")


# Change dictionary item

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

mydict["color2"] = "green"

print(mydict)


# Update dictionary

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

mydict.update({"color2": "green"})

print(mydict)


# Add new item

mydict = {
    "color1": "red",
    "color2": "black"
}

mydict["color3"] = "orange"

print(mydict)


# Add item using update()

mydict = {
    "color1": "red",
    "color2": "black"
}

mydict.update({"color3": "orange"})

print(mydict)


# Remove item using pop()

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

mydict.pop("color2")

print(mydict)


# Remove last inserted item

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

mydict.popitem()

print(mydict)


# Remove item using del

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

del mydict["color2"]

print(mydict)


# Clear dictionary

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

mydict.clear()

print(mydict)


# Delete dictionary

mydict = {
    "color1": "red",
    "color2": "black"
}

del mydict


# Loop through dictionary keys

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

for x in mydict:
    print(x)


# Loop through dictionary values

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

for x in mydict.values():
    print(x)


# Loop through dictionary keys

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

for x in mydict.keys():
    print(x)


# Loop through dictionary items

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

for key, value in mydict.items():
    print(key, value)


# Copy a dictionary

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

newdict = mydict.copy()

print(newdict)


# Copy dictionary using dict()

mydict = {
    "color1": "red",
    "color2": "black",
    "color3": "orange"
}

newdict = dict(mydict)

print(newdict)


# Nested dictionary

mydict = {
    "student1": {
        "name": "Ayesha",
        "age": 20
    },
    "student2": {
        "name": "Ali",
        "age": 22
    }
}

print(mydict)


# Access nested dictionary item

mydict = {
    "student1": {
        "name": "Ayesha",
        "age": 20
    }
}

print(mydict["student1"]["name"])