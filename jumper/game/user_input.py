class User_input:
    """
    An instance that  will promp user for input -verify that it is valid input and
    store the data


    Attributes:
        user_guess (str)            : The guess from the user - a string length 1
        guessed_letters (list)      : The letters that the user has guess in lowercase format
        not_guessed_letters (list)  : The letters of the alphabet that have not been guessed yet - in lower case format

    Methods:
        get_input (self) :          Get the guessed letter from the user, makes sure it is a valid guess then stores it in guessed letter
        update_lists (self) :       Updates the guessed_letters list, the not_guessed_letters, and updates gueseed letter to an empty string   
    """

    def __init__(self):
        self.user_guess = ""
        self.guessed_letters = []
        self.not_guessed_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def get_input(self):
        guess_continue = True


        while guess_continue:
            temp_input = input(f"Guess a letter [a-z]: ")
            lowercase_input  = temp_input.lower()


            if lowercase_input in self.guessed_letters:
                print("I am sorry you have already guessed this letter, please guess again ")

            elif lowercase_input in self.not_guessed_letters:
                self.user_guess = lowercase_input
                guess_continue = False

            else:
                print("You have not entered a valid letter, please enter a single letter guess")
            



    def update_lists(self):
        self.guessed_letters.append(self.user_guess)
        self.guessed_letters.sort()
        self.not_guessed_letters.remove(self.user_guess)
        self.user_guess = ""
