word_definitions = {'pen': [('noun ', 'A writing implement'), ('verb ', 'Write something down')],
              'mobile phone': ['noun A portable telephone'],
              'small': ['adjective Less than average in size']}


# this function suggests a definition
def suggest_definition(word):


    if word in word_definitions:
        print('stage1 is correct')
        return word_definitions[word]
    else:
        possible_match = fuzzy_match(word)
        if possible_match:
            return possible_match
        else:
            return False

def print_definitions(definition):
    if definition != False:
        n = 1
        for this_definition in definition:
            print('{}: {} {}'.format(n, this_definition[0], this_definition[1]))
            n = n + 1
    else:
        print('error')


def fuzzy_match(word):
    matched_definition = False

    for entry in word_definitions:
        if entry in word:
            matched_definition = word.upper() + ' not found\n' + 'Is this what you\'re looking for?\n' + entry + ': ' + str(word_definitions[entry])
            break

    return matched_definition

def anything_else(response):

    if 'yes'in response:
        print('Type to see:\na) this word in a sentence\nb)this word translated into Italian\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')
        #print(something_else(input()))
    elif 'no' in response:
        print('bye')
        exit(0)
    else:
        print('Type to see:\na) this word in a sentence\nb)this word translated into Italian\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')
        #print(something_else(input()))


'''def put_sentence(word):
    sentence = dict()
    sentence = {'pen': ['Circle the answer using a red pen', 'He couldn\'t pen the story'],
                'mobile phone': ['She borrowed her friends mobile phone to call her parents'],
                'small': 'The slice of cake was dissapointingly small'}
    print (sentence[word])'''

lookup_word = input()
definition = suggest_definition(lookup_word)

print(definition)
print_definitions(definition)
print(anything_else(input()))