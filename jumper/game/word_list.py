import random

class word_list:
    def __init__(self):
        self.lines = None
    
    def random_words(self):
        self.lines = open('word_list.txt').read().splitlines()
        randomLine = random.choice(self.lines)
        return(randomLine)