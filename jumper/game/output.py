# Class to hold all the output for the user.
class Output:
    # Initializes variables in the output class
    # A welcome message, the guy with the parachute for the user to see.
    # Lastly, a variable for the guessed letters
    def __init__(self):
        self._welcome = "Welcome to Jumper"
        self._parachute_dude = [' ___', '/___\ ', '\   / ', ' \ / ',
                               '  O ', ' /|\ ', ' / \ ', '      ', '^^^^^^ ']
        self._displayed_letters = "_____"

# This method will print out the welcome message, and the parachute guy
    def parachute_guy(self):
        print(self._welcome)
        for lines in self._parachute_dude:
            print(lines)
# this method will set the correct guesses by the user
# and keep looping through the guesses replacing the underscores. 
    def set_correct_letter(self, user_guess, index):
        listified = list(self._displayed_letters)
        
        for i in index:
            listified[i] = user_guess

        self._displayed_letters = listified
# This method will reset the displayed letters back to underscores
    def reset_displayed_letters(self):
        self._displayed_letters = "_____"
# This method will display the underscores or correct letters and the amount of
# parachute that is left for the user.
    def display(self, missed_guesses):
        print("\n" + " ".join(self._displayed_letters) + "\n")
        for i in range(len(self._parachute_dude)):
            if i >= missed_guesses:
                if missed_guesses == 4 and i == 4:
                    print("  X")
                else:
                    print(self._parachute_dude[i])
                    
                    
# This method will display the winning or losing state for the user. 
    def display_game_over(self, hits, misses):
        self.display(misses)
        if hits == 5 and misses < 4:
            print("You Won! Congratulations!")
        else:
            print("Sorry, you didn't guess the word in time. GAME OVER.")