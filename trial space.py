word_definitions = {
    'pen': [('noun ', 'A writing implement','la penna'),
            ('verb ', 'Write something down', 'lui/lei scrive')],
    'mobile phone': [('noun', 'A portable telephone','il cellulare')],
    'small': [('adjective', 'Less than average in size','piccolo/a')]}


# this function suggests a definition
def suggest_definition(word):


    if word in word_definitions:
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
            print('{}: {}   {}'.format(n, this_definition[0], this_definition[1]))
            n = n + 1
    else:
        print('Sorry I don\'t recognise that word')



def fuzzy_match(word):
    matched_definition = False

    for entry in word_definitions:
        if entry in word:
            matched_definition = word_definitions[entry]
            print(word.upper() + ' not found\n' + 'Is this what you\'re looking for?\n' + entry + ': ')
            break
    return matched_definition

def can_i_help():
    print('Is there anything else I can help you with?')


def anything_else(response):

    if 'yes'in response:
        print('Type to see:\na)this word translated into Italian \nb)this word in a sentence\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')

    elif 'no' in response:
        print('bye')
        exit(0)
    else:
        print('Type to see:\na)this word translated into Italian\nb)this word in a sentence\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')


def something_else(enter):
    if 'translate' in enter:
        print('Please type english word')
        return trans_to_italian(input())
    elif 'sentence' in enter:
        print('incomplete')
    elif 'def' or 'new' in enter:
        print(suggest_definition(input()))
    elif 'alt' in enter:
        print('incomplete')
    else:
        print('try again')
        return something_else(input())

'''def put_sentence(word):
    sentence = dict()
    sentence = {'pen': ['Circle the answer using a red pen', 'He couldn\'t pen the story'],
                'mobile phone': ['She borrowed her friends mobile phone to call her parents'],
                'small': 'The slice of cake was dissapointingly small'}
    print (sentence[word])'''

def trans_to_italian(word):
    n = 1
    if word in word_definitions:
        english =  word_definitions[word]

        for eng_to_ita in english:
            print('{}: {}   {}'.format(n, eng_to_ita[0], eng_to_ita[2]))
            n = n + 1
    else:
        print('Sorry I don\'t recognise that word')
        exit(0)

''' n = 1
    for eng_to_ita in english:
        print('{}: {}   {}'.format(n, eng_to_ita[0], eng_to_ita[2]))
        n = n + 1'''




lookup_word = input()
definition = suggest_definition(lookup_word)
'''translation = trans_to_italian(lookup_word)'''


definition
print_definitions(definition)
can_i_help()
anything_else(input())
something_else(input())