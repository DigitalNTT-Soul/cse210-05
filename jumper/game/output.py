class Output:
    def __init__(self):
        self.welcome = "Welcome to Jumper"
        self.parachute_dude = [' ___', '/___\ ', '\   / ', ' \ / ',
                               '  O ', ' /|\ ', ' / \ ', '      ', '^^^^^^ ']
        self.displayed_letters = "_____"

    def parachute_guy(self):
        print(self.welcome)
        for lines in self.parachute_dude:
            print(lines)

    def set_correct_letter(self, single_char, index):
        if index is list:
            for i in index:
                self.displayed_letters[i] = single_char
        else:
            self.displayed_letters[index] = single_char

    def reset_displayed_letters(self):
        self.displayed_letters = "_____"

    def display(self, missed_guesses):
        print("\n" + " ".join(self.displayed_letters) + "\n")
        for i in range(len(self.parachute_dude)):
            if i >= missed_guesses:
                if missed_guesses == 4 and i == 4:
                    print("  X")
                else:
                    print(self.parachute_dude[i])


output = Output()

output.parachute_guy()
output.display(1)
output.display(2)
output.display(3)
output.display(4)
