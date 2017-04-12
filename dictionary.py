letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


word_definitions = {'pen': [('noun ', 'A writing implement'), ('verb ', 'Write something down')],
              'mobile phone': ['noun A portable telephone'],
              'small': ['adjective Less than average in size']}


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

def fuzzy_match(word):

    for entry in word_definitions:
        if entry in word:
            return word.upper() + ' not found\n' + 'Is this what you\'re looking for?\n' + entry + ': ' + str(word_definitions[entry])
    return False


#offers more features
def anything_else(response):

    if 'yes'in response:
        print('Type to see:\na) this word in a sentence\nb)this word translated into Italian\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')
        print(something_else(input()))
    elif 'no' in response:
        print('bye')
        exit(0)
    else:
        print('Type to see:\na) this word in a sentence\nb)this word translated into Italian\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')
        print(something_else(input()))

def put_sentence(word):
    sentence = dict()
    sentence = {'pen': ['Circle the answer using a red pen', 'He couldn\'t pen the story']}
    print (sentence[word])

def translate(word):
    italian = dict()
    italian = {'pen': ['la penna']}
    return italian['pen']

def something_else(enter):
    sentence = dict()
    sentence = {'pen': ['Circle the answer using a red pen', 'He couldn\'t pen the story']}
    if 'sentence' in enter:
              return put_sentence(enter)
    elif 'translate' in enter:
              return translate(enter)
    else:
              return 'other'



anything ='Is there anything else we can help you with?'
suggested_definition =suggest_definition(input())
if suggested_definition != False:
    print(suggested_definition)
else:
    print('Word not found, enter a new word')


print(anything)
print(anything_else(input()))