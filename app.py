triangles = {}

def addTriangle():
    name = raw_input("Enter name: ")
    a = int(raw_input("Enter a: "))
    b = int(raw_input("Enter b: "))
    c = int(raw_input("Enter c: "))
    if is_valid(a, b, c):
        triangles[square(a, b, c)] = name
        print "Triangle is valid"
        to_continue()
    else:
        print "Triangle is invalid"
        to_continue()


def is_valid(a, b, c):
    if a<0 or b<0 or c<0 or a>=(c+b) or b>=(a+c) or c>=(a+b):
        return False
    else:
        return True


def square(a, b, c):
    p = (a + b + c) / 2.0
    square = (p*(p-a)*(p-b)*(p-c))**0.5
    return square


def to_continue():
    cont = raw_input("Do you want to continue? ")
    if cont.lower() == "y" or cont.lower() == "yes":
        addTriangle()
    else:
        print_sorted()


def print_sorted():
    squares = triangles.keys()
    squares.sort()
    squares = squares[::-1]
    print "-Triangle-"
    for i in squares:
        print "%s: %s" %(triangles[i], i)

addTriangle()