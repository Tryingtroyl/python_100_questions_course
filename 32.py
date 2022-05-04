c = 1
def foo():
    return c
c = 3
print(foo())

#The output is 3 as c is globally changed to 3