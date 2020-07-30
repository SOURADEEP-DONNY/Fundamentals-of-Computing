# Arithmetic expressions - numbers, operators, expressions

#print 3, -1, 3.14159, -2.8

# numbers - two types, an integer or a decimal number
# two corresponding data types int() and float()

print (type(3), type(3.14159))
print (type(3.0))


# we can convert between data types using int() and float()
# note that int() takes the "whole" part of a decimal number and doesn't round
# float() applied to integers is boring

print (int(3.14159), int(-2.8))
print (float(3), float(-1))


# floating point number have around 15 decimal digits of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.4142135623730950488016887242096980785696...

# approximation of pi, Python displays 12 decimal digits

print (3.1415926535897932384626433832795028841971)

# appoximation of square root of two, Python displays 12 decimal digits

