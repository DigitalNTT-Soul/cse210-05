class Output:
    def __init__(self):
        self._welcome = "Welcome to Jumper"
        self._parachute_dude = [' ___', '/___\ ', '\   / ', ' \ / ',
                               '  O ', ' /|\ ', ' / \ ', '      ', '^^^^^^ ']
        self._displayed_letters = "_____"

    def parachute_guy(self):
        print(self._welcome)
        for lines in self._parachute_dude:
            print(lines)

    def set_correct_letter(self, user_guess, index):
        listified = list(self._displayed_letters)
        
        for i in index:
            listified[i] = user_guess

        self._displayed_letters = listified

    def reset_displayed_letters(self):
        self._displayed_letters = "_____"

    def display(self, missed_guesses):
        print("\n" + " ".join(self._displayed_letters) + "\n")
        for i in range(len(self._parachute_dude)):
            if i >= missed_guesses:
                if missed_guesses == 4 and i == 4:
                    print("  X")
                else:
                    print(self._parachute_dude[i])
                    
    def display_game_over(self, hits, misses):
        self.display(misses)
        if hits == 5 and misses < 4:
            print("You Won! Congratulations!")
        else:
            print("Sorry, you didn't guess the word in time. GAME OVER.")