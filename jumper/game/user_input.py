class User_input:
    """
    An instance that  will promp user for input -verify that it is valid input and
    store the data


    Attributes:
        user_guess (str)            : The guess from the user - a string length 1
        guessed_letters (list)      : The letters that the user has guess in lowercase format
        not_guessed_letters (list)  : The letters of the alphabet that have not been guessed yet - in lower case format


    """

    def __init__(self):
        self.user_guess = ""
        self.guessed_letters = []
        self.not_guessed_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def get_input(self):
        pass

    def update_lists(self):
        pass
