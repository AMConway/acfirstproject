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


'''def nice_formatting(word_definitions[lookup_word]):
    if suggested_definition != False:
        print('There are {} definitions for {} in the dictionary.'.format(len(suggested_definition), lookup_word))
        for speech, description in enumerate.(word_definitions[lookup_word]):
            print('{} {}'.format(speech, description))
            return'''





'''if suggested_definition != False:
    #print(suggested_definition)
    print('There are {} definitions for {} in the dictionary.'.format(len(suggested_definition), lookup_word))
    for definition in suggested_definition:
        print('   Definition {} has {} parts to it.'.format(definition, len(definition)))
else:
    print('Word not found, enter a new word')

for speech, description in enumerate.(suggested_definition):
    print(speech,description)'''

anything = 'Is there anything else we can help you with?'

if len(suggested_definition) ==1:
    # problem here
    ''' else :
        print('There are {} definitions for {} in the dictionary.'.format(len(suggested_definition), lookup_word))
        print('{}.{}\n{}.{}'.format((len(suggested_definition) - 1), possible_definitions[0],
                                    len(suggested_definition), possible_definitions[1]))'''

    n = len(definition)
    if definition != False:
        for i in range(n):
            while n > 0:
                n = n - 1
                print(n * ('{}').format(n, definition(n)))
