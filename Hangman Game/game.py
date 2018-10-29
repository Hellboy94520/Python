from functions import *
from tools import to_string

def new_game():
    """ --- Variables --- """
    attempt = 8
    word_to_guess = []
    word_guessing = []
    letter_used = []
    success = False

    """ --- Preparation --- """
    #Generate a random word
    word_to_guess = get_word() 
    #Create a word with the same quantity letter but replace by dash
    word_guessing = get_word_with_dash(word_to_guess)
    
    print("Let's go ! Guess the word !")

    """ -- Begin Game -- """
    while attempt!=0:
        
        letter_used.append(get_character(letter_used))
        
        if letter_used[-1] in word_to_guess:
            word_guessing = add_characters_founded(word_guessing, word_to_guess, letter_used)
            print("YES ! You find the letter : {} ".format(letter_used[-1]))
            if word_guessing == word_to_guess:
                success=True
                break
        else:
            attempt-=1
            print("WRONG ! You have {} attempt left(s)".format(attempt))
        
        print("You used : {}".format(letter_used))
        print("You find : {} ".format(to_string(word_guessing)))
        print("************")
    
    """ --- Game Over --- """
    if success is True:
        print("You find the word {} ! You win this game !".format(to_string(word_guessing)))
        return True
    else:
        print("You loose this game ! You do not find \'{}\', sorry !".format(to_string(word_to_guess)))
        return False