# dictionary
a = {'x': 1, 'y': 2, 'z': 3}
print a
print a['x']
print a['y']
b = {}
b['x'] = 2
print b
b[2] = 'foo'
print b
b[(1, 2)] = 3
print b

# 'del' keyword can be used to delete an item from a dictionary
del a['x']
print a

# 'keys' method return all keys in a dictionary
# 'values' method returns all values in a dictionary
# 'items' method returns all key-value pairs in a dictionary
print a.keys()
print a.values()
print a.items()

# 'for' statement can be used to iterate over a dictionary
for key in a:
	print key

for key, value in a.items():
    print key, value

# 'has_key' method and 'in' operator can test the presence of a key in a dictionary
print 'x' in a
print 'y' in a
print a.has_key('x')
print a.has_key('y')

# 'get' method can return the value of the key if the key in the dictionary
# ,else default. If default not given, value default to None.
d = {'x': 1, 'y': 2, 'z': 3}
print d
print d.get('x', 5)
print d.get('p', 5)

# 'setdefault' method, if 'key' in the dictionary, return its value;
# if not, insert 'key' with the 'default' value and return 'default',
# 'default' default to None.
print d.setdefault('x', 0)
print d
print d.setdefault('p', 0)
print d

# dictionary can be used in string formatting to specify named parameters.
print 'hello %(name)s' % {'name': 'python'}
print 'Chapter %(index)d: %(name)s' % {'index': 2, 'name': 'Data Structures'}


# count the frequency of words
def word_frequency(words):
    """return the frequency of each word given a list of words"""

    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


def read_words(filename):
    return open(filename).read().split()


def main(filename):
    frequency = word_frequency(read_words(filename))
    for k, v in frequency.items():
        print k, v

main("foo.txt")

print globals()

