# imports
import random
import numpy as np

import string




# words 

words = ['test', 'cat', 'dog', 'lamp']

# game 
## the task 

word = words[random.randint(0,len(words)-1)]

length = len(word)
hidden_word = '_'*length
shown_word = hidden_word

print('Hi! here is what you need to guess: ' + hidden_word + ' \n')

## input 

# letter = input('Guess letter: ')

def open_letter(letter, word, shown_word): 
    # indices = np.where(array > 5)[0] = 
    word = np.array(list(word))
    if letter in word: 
        indices = np.where(word == letter)
        shown_word = np.array(list(shown_word))
        shown_word[indices] = letter
        shown_word = ''.join(shown_word)
    print(shown_word)
    return shown_word

# Create a set of all lowercase letters
letters_set = set(string.ascii_lowercase)

print(letters_set - 'a')

# drawing
def draw_next(state):
    hangman = '''
      _
      | 
      o
     /|\\
     | |
    '''
    count = 0
    for i in range(len(hangman)):
        if hangman[i] == ' ' or hangman[i] == '\n':
            pass
        elif count == state: break
        else: 
            count +=1
            # print('i',i)
    return hangman[:i]
        

# the game process
state = 0
while state < 8: 
    letter = input('Ok. Guess next letter: ')
    if letter in word:
        shown_word = open_letter(letter, word, shown_word)
        if '_' not in shown_word: print('Congrats! You won, word is', shown_word)
    else: 

        state += 1
        print('nope, you made ' + str(state) + ' errors')
        print(draw_next(state))
        
    #todo add 

print('Congrats! You lost')



