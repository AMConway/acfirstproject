letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


word_definitions = {'pen': [('noun ', 'A writing implement'), ('verb ', 'Write something down')],
              'mobile phone': ['noun A portable telephone'],
              'small': ['adjective Less than average in size']}

possible_definitions = (word_definitions[input()])
# this function suggests a definition
def suggest_definition(word):


    if word in word_definitions:

        return possible_definitions
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
        #print(something_else(input()))
    elif 'no' in response:
        print('bye')
        exit(0)
    else:
        print('Type to see:\na) this word in a sentence\nb)this word translated into Italian\nc)' \
                       'a definition of a new word\nd)suggest an alternative definition to this word')
        #print(something_else(input()))'''

#notcomplete
'''def put_sentence(word):
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
              return 'other'''''

lookup_word = input()
anything ='Is there anything else we can help you with?'
suggested_definition =suggest_definition(lookup_word)

if suggested_definition != False:
         print('There is {} definitions for {} in the dictionary.'.format(len(suggested_definition), lookup_word))

         if len(suggested_definition) ==1:
             print('{}.{}'.format((len(suggested_definition) - 1), possible_definitions[0])
#problem here
         else :
             print('There are {} definitions for {} in the dictionary.'.format(len(suggested_definition), lookup_word))
             print('{}.{}\n{}.{}'.format((len(suggested_definition) - 1), possible_definitions[0],
                                         len(suggested_definition), possible_definitions[1]))


      #for speech, definition in lookup_word:
             # print('{}\n {}'.format(word_definitions[word[0]], word_definitions[word[1]])
             # print('Word not found, enter a new word')


print(anything)

print(anything_else(input()))