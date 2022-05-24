from input import Input
from output import Output
from word_list import Word_list

class Director:
    def __init__(self):
        self._input = Input()
        self._output = Output()
        self._word_list = Word_list()
        self._missed_guesses = 0
        self._guess = ""
        self._play_new_round = True

    def start_game(self):
        while True:
            self._input.set_word(self._word_list.get_random_word())
            self._output.reset_displayed_letters()
            while self._play_new_round and self._missed_guesses < 4:
                # Display gamestate
                self._output.display(self._missed_guesses)

                # Get user's guess
                self._guess = self._input.get_guess()
                
                # See if user's guess was correct (function should return number of matches and list of match indices)
                match_count, indices = self._input.validate(self._guess)

                if match_count == 0:
                    self._missed_guesses += 1
                else:
                    self._output.set_correct_letter(self._guess, indices)

            # need some sort of game over message perhaps? maybe
            self._play_new_round = self._input.prompt_play_again()