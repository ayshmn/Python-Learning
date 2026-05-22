# 1. Arithmetic Operators

a = 8
b = 4
print(a+b) # Addition
print(a-b) # Substraction
print(a*b) # Multiplication
print(a/b) # Division
print(a%b) # Modulus
print(a**b) # Exponentiation
print(a//b) # Floor division


# 2. Assignment Operators

a = 2 
print(a)

a = 6
a += 6
print(a)

a = 6
a -= 6
print(a)

a = 6
a *= 6
print(a)

a = 6
a /= 6
print(a)

a = 6
a %= 6
print(a)

a = 6
a //= 6
print(a)

a = 6
a **= 6
print(a)

a = 6
a &= 6
print(a)

a = 6
a |= 6
print(a)

a = 6
a ^= 6
print(a)

a = 6
a >>= 6
print(a)

a = 6
a <<= 6
print(a)

a = 6
print(x := a)


# 3. Comparision Operator

a = 5
b = 10

print(a==b) # Equal
print(a!=b) # Not equal
print(a>b) # Greater Than
print(a<b) # Less than
print(a<=b) # Less than equal to
print(a>=b) # Greater than equal to


# 4. Logical Operators

a = 10 
b = 5

print(a<b and a>b) # and
print(a<b or a>b) # or
print(not(a<b and a>b)) # not


# 5. Bitwise Operator

a = 9
b = 3

print(a&b) # AND
print(a|b) # OR
print(a^b) # XOR
print(~a) # NOT
print(a<<b) # Zero fill left shift
print(a>>b) #Signed right shift


# 6. Identify Operator

# is example

a = ["apple" , "banana"]
b = ["apple" , "banana"]
c = a

print(a is c) 
print(a is c)

# is not example

a = ["apple" , "banana"]
b = ["apple" , "banana"]
c = a

print(a is not c) 
print(a is not c)


# 7. Membership Operators

# in example

a =  ["apple" , "banana"] 
print("banana" in a)


# not in example

a =  ["apple" , "banana"] 
print("orange" not in a)