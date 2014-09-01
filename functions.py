# a piece of logic can also be associated with a name by defining a function
def square(x):
    return x * x

# functions can be used in any expressions
print square(2) + square(3)
print square(square(3))


# exsiting functions can be used in creating new functions.
def sum_of_squares(x, y):
    return square(x) + square(y)

print sum_of_squares(2, 3)


# functions can be assigned, passed as arguments to other functions etc.
f = square
print f(4)


def fxy(f, x, y):
    return f(x) + f(y)

print fxy(square, 2, 3)


# it is important to understand the scope of the variables used in functions.
# example
x = 0
y = 0
print "x =", x
print "y =", y


def incr(x):
    y = x + 1
    return y

incr(5)
print "x, y =", x, y


# python sees use of a variable not defined locally, it tries to find a
# global variable with that name.
pi = 3.14


def area(r):
    return pi * r * r

print "area of r = 1:", area(1)


# however, you have to explicitly declare a variable as 'global' to modify it.
numcalls = 0


def square(x):
    global numcalls
    numcalls += 1
    return x * x

print "numcalls =", numcalls
print "square(2) =", square(2)
print "numcalls =", numcalls


# functions called with keyword arguments
def difference(x, y):
    return x - y

# same ends of the following four forms
print difference(5, 2)
print difference(x=5, y=2)
print difference(5, y=2)
print difference(y=2, x=5)



# functions can have default values
def increment(x, amount=1):
    return x + amount

# same ends of the following four forms
print increment(10)
print increment(10, 5)
print increment(10, amount=2)
print increment(amount=2, x=10)



# built-in functions
print min(2, 3)
print max(2, 3)
print len('helloworld')
# int converts string to ingeter and str converts integers and other type of objects to strings
print int('50') + 1
print str(123)



# practice
def count_digits(x):
	return len(str(x))

print count_digits(5)
print count_digits(12345)



# methods
# methods are special kind of functions that work on an object.
# 'upper' is  a  method available on string objects.
x = 'hello'
print x.upper()

# methods are also functions, they can be assigned to other variables can be call separately
f = x.upper
print f(), x.upper()



# istrcmp to compare two strings, ignoring the case
def istrcmp(x, y):
	return cmp(x, y)

print istrcmp('python', 'Python')





































