import random
import os

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
        """
        Constructor to open file into a list for future use by getter method
        """
        self._file = None # stores the object, not the filename
        self._lines = []

        # get path to the word_list.txt file
        path_to_here = os.path.abspath(__file__)
        path_to_list = os.path.join(os.path.dirname(path_to_here), 'word_list.txt')

        with open(path_to_list, 'r') as self._file:
            self._lines = self._file.read().splitlines()
    
    def get_random_word(self):
        """
        simple getter to return a random word from the list
        """
        return random.choice(self._lines)