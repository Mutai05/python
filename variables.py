#!/usr/bin/python3

# Creating Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

name = "Mutai Kelvin"
age = 27

print(name)
print(age)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4
x = "Ess K"
print(x)


# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))


# Case-Sensitive
# Variable names are case-sensitive.
# This will create two variables:
# A will not overwrite a

a = 4
A = "Ess K"

print(a)
print(A)


# Variable names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)