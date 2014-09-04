# list
# built-in function 'range' can be used to create a list of integers
print range(4)
print range(3, 6)
print range(2, 10, 3)


# built-in function 'len' can be used to find the length of a list
a = [1, 2, 3, 4]
print len(a)


# '+' and '*' operators work even on lists
a = [1, 2, 3]
b = [4, 5]
print "a =", a
print "b =", b
print "a + b =", a + b
print "b * 3 =", b * 3


# use list slicing to get part of a list
x = [1, 2, 3, 4]
this slice don`t contain the last location
print x[0:2]
print x[1:4]
print x[0:-1]
omitted first index is zero, omitted second index defaults to the size
of the list being sliced
print x[:]
optional third index can be used to specify the increment, which default to 1
x = range(10)
print x
print x[0:6:2]
provide -1 increment can reverse a list
print x[::-1]


# list members can be modified by assignment
x = [1, 2, 3, 4]
print x
x[1] = 5
print x


# 'in' operator can test the pressence of a key in a list
x = [1, 2, 3, 4]
print 2 in x
print 10 in x


# practice
x = [0, 1, [2]]
x[2][0] = 3
print x
x[2].append(4)
print x
x[2] = 2
print x


# python provide 'for' statement to iterate over a list. A 'for' statement
# executes the specified block of code for every element in a list.
for x in [1, 2, 3, 4]:
    print x

for i in range(10):
    print i, i * i, i * i * i


# built-in function 'zip' takes two lists and returns list of pairs.
x = ['a', 'b', 'c']
y = [1, 2, 3]
print x, y
print zip(x, y)
it is handy when we want to iterate over two lists together.
names = ['a', 'b', 'c']
values = [1, 2, 3]
for name, value in zip(names, values):
    print name, value


# practice
def sum(x):
    sum = ''
    for a in x:
        sum += a
    return sum

print sum([1, 2, 3])
print sum(['hello', 'world'])
print sum(['aa', 'bb', 'cc'])


# list Comprehensions
# list comprehensions provide a concise way of creating lists.
a = range(10)
print a
print[x for x in a]
print[x * x for x in a]
print[x + 1 for x in a]

# It is possible to filter a list using 'if' inside a list comprehension
a = range(10)
print a
print[x for x in a if x % 2 == 0]
print[x * x for x in a if x % 2 == 0]

# It is possible to iterate over multiple lists using the built-in
# function 'zip'.
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
print zip(a, b)
print[x + y for x, y in zip(a, b)]

# we can use multiple 'for' clause in single list comprehension.
print[(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0]
print[(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0 and x != y]
