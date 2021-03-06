# working with files
# built-in function 'open' can open a file and return a file object
# easiest way to read contents of a file is using the 'read' method
print open('foo.txt', 'r').read()
print open('foo.txt', 'r').readlines()
# 'readline' method returns empty string when there is nothing more
# to read in a file.
f = open('foo.txt', 'r')
print f.readline()
print f.readline()
print f.readline()
print f.readline()
f.close()


# 'write' method is used to write data to a file opened in write or append mode.
f = open('foo.txt', 'w')
f.write('a\nb\nc')
f.close()

f = open('foo.txt', 'a')
f.write('d\n')
f.close()


# 'writelines' method is convenient to use when the data is
# available as a list of lines.
f = open('foo.txt', 'w')
f.writelines(['aa\n', 'bb\n', 'cc\n'])
f.close()


practice
# count


def charcount(filename):
    return len(open(filename).read())


def wordcount(filename):
    return len(open(filename).read().split())


def linecount(filename):
    return len(open(filename).readlines())


print charcount('foo.txt')
print wordcount('foo.txt')
print linecount('foo.txt')


# print lines in reverse order
def reverse(x):
    linelist = open(x, 'r').readlines()
    linelist.reverse()
    for line in linelist:
        print line.strip('\n')

reverse('foo.txt')


