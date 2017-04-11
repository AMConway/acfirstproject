import math

def volume_sphere(radius):
    pi = math.pi
    volume = 4/3 * pi * radius**3
    return volume

print(volume_sphere(5))


def wholesale(copies):

    per_book = 0.6*24.95*copies
    shipping = 3 + (0.75*(copies-1))

    return per_book + shipping

print(wholesale(60))

print(int(7.9))
print(float(37))

def right_justify(s):
    justify = (70-len(s))*" "
    return justify + s

print(right_justify("monty"))

def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')

print(do_twice(print_spam))



def define(word):
    definition = '1.noun A writing implement'
    return(word + definition)

print(define('pen'))