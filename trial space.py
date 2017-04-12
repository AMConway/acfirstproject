word_definitions = {
    'pen': [('noun ', 'A writing implement','la penna','Circle the answer using a red pen'),
            ('verb ', 'Write something down', 'lui/lei scrive', 'He couldn\'t pen the story')],
    'mobile phone': [('noun', 'A portable telephone','il cellulare','She borrowed her friend\'s mobile phone '
                                                                    'to call her parents')],
    'small': [('adjective', 'Less than average in size','piccolo/a','The slice of cake was dissappointingly small')],
    'quickly': [('adverb', 'to do something at a fast pace', 'velocemente', 'They ran so quickly they were home before the bus'
                 )]}



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

    if 'no' in response:
        print('bye')
        exit(0)
    else:
        print('Type to see:\na)this word translated into Italian\nb)this word in a sentence\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition for this word')


def something_else(enter):
    if 'translate' in enter:
        print('Please type english wordA')
        return trans_to_italian(input())
    elif 'sentence' in enter:
        print('Please type english wordB')
        return put_sentence(input())
    elif 'new' in enter:
        print('Please type english wordC')#stuck on line 30
        return(print_definitions(input()))
    elif 'alt' in enter:
        print('incomplete')
    else:
        print('try again')
        return something_else(input())



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


def put_sentence(word):
    n = 1
    if word in word_definitions:
        english = word_definitions[word]

        for in_sentence in english:
            print('{}: {}   {}'.format(n, in_sentence[0], in_sentence[3]))
            n = n + 1
    else:
        print('Sorry I don\'t recognise that word')
        exit(0)




print('Please type an english word to get a definition')
lookup_word = input()
definition = suggest_definition(lookup_word)
print_definitions(definition)



while True:
    can_i_help()
    response = input()
    if 'no' in response:
        print('bye')
        break
    else:
        print('Type to see:\na)this word translated into Italian\nb)this word in a sentence\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition for this word')
        response = input()
        if 'translate' in response:
            print('Please type english wordA')
            trans_to_italian(input())
        elif 'sentence' in response:
            print('Please type english wordB')
            put_sentence(input())
        elif 'new' in response:
            print('Please type english wordC')  # stuck on line 30
            print_definitions(input())
        elif 'alt' in response:
            print('TODO: incomplete')
        else:
            print('Unrecognised. Please try again')

