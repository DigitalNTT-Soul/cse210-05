from game.user_input import User_input
from game.output import Output
from game.word_list import Word_list

class Director:
    """
    Director class: Responsible for handling the main gameplay loop and passing information
        and delegated tasks from module to module    
    """
    def __init__(self):
        """
        Constructor to declare relevant attributes
        """
        self._input = User_input()
        self._output = Output()
        self._word_list = Word_list()
        self._misses = 0
        self._hits = 0
        self._guess = ""
        self._play_new_round = True

    def start_game(self):
        """
        Main gameplay loop
        Suitable for multiple rounds of gameplay, so that the user doesn't need to relaunch the
            game software to play a new round
        """
        while self._play_new_round:
            self._input.set_word(self._word_list.get_random_word())
            self._output.reset_displayed_letters()
            self._input.reset_guessed_letters()
            self._misses = 0
            self._hits = 0

            while self._hits < 5 and self._misses < 4:
                # Display gamestate
                self._output.display(self._misses)

                # Get user's guess
                self._input.get_input()
                self._guess = self._input.user_guess
                self._input.update_lists()
                
                # See if user's guess was correct (function should return number of matches and list of match indices)
                match_count, indices = self._input.check_guess_in_word(self._guess)
                self._hits += match_count

                if match_count == 0:
                    self._misses += 1
                else:
                    self._output.set_correct_letter(self._guess, indices)

            # need some sort of game over message perhaps? maybe
            self._output.display_game_over(self._hits, self._misses)
            self._play_new_round = self._input.prompt_play_again()