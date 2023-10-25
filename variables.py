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
my_var = "Kelvin"
_my_var = "Ess K"
myVar = "Mutai"
MYVAR = "Sharon"
myvar2 = "Joy"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "Mango"

print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["Melon", "Apple", "Passion"]
x, y, z = fruits

print(x)
print(y)
print(z)

# Output variables
# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "Awesome"

print(x, y, z)

# You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "Easy"

print(x + y + z)