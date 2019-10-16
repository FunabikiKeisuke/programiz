# Note: You may get different value of id
a = 2

# Output: id(2) = 140723380855216
print('id(2) =', id(2))

# Output: id(a) = 140723380855216
print('id(a) =', id(a))


# Note: You may get different value of id
a = 2

# Output: id(a) = 140723380855216
print('id(a) =', id(a))

a = a+1

# Output: id(a) = 140723380855248
print('id(a) =', id(a))

# Output: id(3) = 140723380855248
print('id(3) =', id(3))

b = 2

# Output: id(2) = 140723380855216
print('id(2) =', id(2))


def printHello():
    print("Hello")
a = printHello()

# Output: Hello
a