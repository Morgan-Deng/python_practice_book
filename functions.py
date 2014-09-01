# a piece of logic can also be associated with a name by defining a function
def square(x):
	return x*x

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
	return f(x)+f(y)

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

# python sees use of a variable not defined locally, it tries to find a global variable with that name.
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

print "numcalls =",numcalls
print "square(2) =",square(2)
print "numcalls =",numcalls