from data import word_list
from random import choice

""" -- Check size, the ascii_code and if the character is already used -- """
def check_input_letter(character, character_list):
    try:
        ascii_code = ord(character)
        assert ascii_code>=94
        assert ascii_code<123
    except AssertionError:
        print("ERROR ! Waiting only a tiny alphabetic character !")
        return False
    except:
        print("ERROR ! Waiting only one character !")
        return False
    
    if character in character_list:
        print("ERROR ! This character is already used !")
        return False
    return True

""" -- Return a random word of the list -- """
def get_word():
    return choice(word_list)

""" -- Ask to input a character and check it -- """
def get_character(character_used):
    character = ""
    while character=="" or check_input_letter(character, character_used) is False:
        character = input("Input a character : ")
    return character

""" -- Create a word with exact same size but with only dash -- """
def get_word_with_dash(word):
    dashword = []
    for i in word:
        dashword.append("-")
    return dashword

""" -- Replace any characters founded of the word input, by the characters of the second word -- """
def add_characters_founded(word_guessing, word_to_guess, characters_founded):
    for i, character in enumerate(word_to_guess):
        if character in characters_founded:
            word_guessing[i]=character
    return word_guessing