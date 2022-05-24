import random

class Word_list:
    """
    Gathers and contains the list of all words used for the game, as well as 
        offering a function for getting a random word from that list
    
    Public Attributes:
        None
    
    Public Methods
        get_random_word(self)       returns whole word as a string.
    """
    def __init__(self):
        self._file = None
        self._lines = None

        with open('word_list.txt') as self._file:
            self._lines = self._file.read().splitlines()
    
    def get_random_word(self):
        return(random.choice(self._lines))