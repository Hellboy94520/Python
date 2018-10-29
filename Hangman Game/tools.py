""" -- Convert a tab to string -- """
def to_string(tab):
    word = ""
    for i in tab:
        word += i
    return word

""" -- Check if the word input is inside the list -- """
def is_waiting(word, resultList):
    for result in resultList:
        if word==result:
            return True
    return False