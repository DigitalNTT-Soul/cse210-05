class Output:
    def __init__(self):
        self._welcome = "_welcome to Jumper"
        self._parachute_dude = [' ___', '/___\ ', '\   / ', ' \ / ',
                               '  O ', ' /|\ ', ' / \ ', '      ', '^^^^^^ ']
        self._displayed_letters = "_____"

    def parachute_guy(self):
        print(self._welcome)
        for lines in self._parachute_dude:
            print(lines)

    def set_correct_letter(self, single_char, index):
        if index is list:
            for i in index:
                self._displayed_letters[i] = single_char
        else:
            self._displayed_letters[index] = single_char

    def reset__displayed_letters(self):
        self._displayed_letters = "_____"

    def display(self, missed_guesses):
        print("\n" + " ".join(self._displayed_letters) + "\n")
        for i in range(len(self._parachute_dude)):
            if i >= missed_guesses:
                if missed_guesses == 4 and i == 4:
                    print("  X")
                else:
                    print(self._parachute_dude[i])
                    
