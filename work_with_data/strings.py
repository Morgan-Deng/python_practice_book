# Strings also behave like lists in many ways.
# 'split' method can splits a string using a delimiter.
# If no delimiter is specified, it uses any whitespace char as delimiter.
x = 'hello deng'
y = 'a,b,c'
print x.split()
print y.split(',')


# 'join' method joins a list of Strings
x = ' '.join(['hello', 'world'])
y = ','.join(['a', 'b', 'c'])
print x
print y
