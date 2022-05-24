import csv
import random

class word_list:
    def random_words(self):
        with open('word_list.csv') as word_list_file :
         word_reader = csv.reader(word_list_file)
    
        word_choice = list(word_reader)[1:]
        random.shuffle(word_choice)

        for name in word_reader:
            print(name)