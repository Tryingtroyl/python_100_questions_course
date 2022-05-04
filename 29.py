import math
def volume(h,r=10):
    return ((4*math.pi*r*r*r)/3)-(math.pi*h*h*((3*r)-h))/3

print(volume(2))