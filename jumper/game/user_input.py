class User_input:
    """
    An instance that  will promp user for input -verify that it is valid input and
    store the data


    Attributes:
        user_guess (str)            : The guess from the user - a string length 1
        guessed_letters (list)      : The letters that the user has guess in lowercase format
        _word (string)              : Five letter word passed in from director

    Methods:
        get_input (self) :          Get the guessed letter from the user, makes sure it is a valid guess then stores it in guessed letter
        update_lists (self) :       Updates and sorts the guessed_letters list, and clears guessed letter back to an empty string   
    """

    def __init__(self):
        """
        Constructor to declare attributes
        """
        self.user_guess = ""
        self.guessed_letters = []
        self._word = ""

    def get_input(self):
        """
        Prompt the user to enter a letter
        Don't let the user guess the same letter multiple times
        Saves guessed letter to public attribute for other sources to pull from.
        """
        guess_continue = True


        while guess_continue:
            temp_input = input(f"Guess a letter [a-z]: ")
            lowercase_input  = temp_input.lower()


            if lowercase_input in self.guessed_letters:
                print("I am sorry you have already guessed this letter, please guess again ")

            elif lowercase_input.isalpha() and len(lowercase_input) == 1:
                self.user_guess = lowercase_input
                guess_continue = False

            else:
                print("You have not entered a valid letter, please enter a single letter guess")
            



    def update_lists(self):
        """
        updates and sorts the list of guessed letters
        clears user_guess back to an empty string
        """
        self.guessed_letters.append(self.user_guess)
        self.guessed_letters.sort()
        self.user_guess = ""

    def check_guess_in_word(self, letter):
        """
        Determines the number of times the provided letter occurs in the solution word
        Locates the indices of those matches
        Returns number of matches and indices of matches
        """
        match_count = self._word.count(letter)
        indices = []
        for i in range(len(self._word)):
            if self._word[i] == letter:
                indices.append(i)

        return match_count, indices

    def set_word(self,word):
        """
        Setter to change what thes olution word itself is.
        """
        self._word = word

    def prompt_play_again(self):
        """
        prompts the user whether they would like to play again, returning True or False
        """
        while True:
            user_response = input(f"would you like to play the game again? (y or n): ")
            if user_response.lower() == "y":
                return True
            elif user_response.lower() == "n":
                return False
            else:
                print("I am sorry that was not a valid response please respond y or n")

    def reset_guessed_letters(self):
        """
        Resets the lsit of guessed letters, to prepare for new rounds
        """
        self.guessed_letters = []