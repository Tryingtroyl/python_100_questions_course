c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

#The output is 2 as the local variable c is given higher precedence