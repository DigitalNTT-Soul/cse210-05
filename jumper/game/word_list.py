import random

class Word_list:
    def __init__(self):
        self._file = None
        self._lines = None

        with open('word_list.txt') as self._file:
            self._lines = self._file.read().splitlines()
    
    def get_random_word(self):
        return(random.choice(self._lines))