# Class to hold all the output for the user.
class Output:
    
    def __init__(self):
        """
        Initializes variables in the output class
        A welcome message, the guy with the parachute for the user to see.
        Lastly, a variable for the guessed letters
        """
        self._welcome = "Welcome to Jumper"
        self._parachute_dude = [' ___', '/___\ ', '\   / ', ' \ / ',
                               '  O ', ' /|\ ', ' / \ ', '      ', '^^^^^^ ']
        self._displayed_letters = "_____"

    
    def parachute_guy(self):
        """
        This method will print out the welcome message, and the parachute guy
        """
        print(self._welcome)
        for lines in self._parachute_dude:
            print(lines)

     
    def set_correct_letter(self, user_guess, index):
        """
        this method will set the correct guesses by the user
        and keep looping through the guesses replacing the underscores.
        """
        listified = list(self._displayed_letters)
        
        for i in index:
            listified[i] = user_guess

        self._displayed_letters = listified

    def reset_displayed_letters(self):
        """
        This method will reset the displayed letters back to underscores
        """
        
        self._displayed_letters = "_____"

    
    def display(self, missed_guesses):
        """
        This method will display the underscores or correct letters and the amount of
        parachute that is left for the user.
        """
        print("\n" + " ".join(self._displayed_letters) + "\n")
        for i in range(len(self._parachute_dude)):
            if i >= missed_guesses:
                if missed_guesses == 4 and i == 4:
                    print("  X")
                else:
                    print(self._parachute_dude[i])

    def display_game_over(self, hits, misses):
        """
        This method will display the winning or losing state for the user.
        """
        self.display(misses)
        if hits == 5 and misses < 4:
            print("You Won! Congratulations!")
        else:
            print("Sorry, you didn't guess the word in time. GAME OVER.")