class Parachute:
    def __init__(self):
        self.welcome = "Welcome to Parachute"
        self.parachute_dude = [' ___', '/___\ ', '\   / ', ' \ / ',
                               '  O ', ' /|\ ', ' / \ ', '      ', '^^^^^^ ']

    def parachute_guy(self):
        print(self.welcome)
        for lines in self.parachute_dude:
            print(lines)

    def remove_line(self):
        print("update this later.")


parachute = Parachute()
parachute.parachute_guy()

