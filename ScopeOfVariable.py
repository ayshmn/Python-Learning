# Local scope of variable

def display():
    name = "Ayesha"
    print(name)

display()


# Globle scope of variable

name = "Ayesha"

def display():
    print(name)

display()