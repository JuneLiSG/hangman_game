# will need to take an input (letter) and check it against the word (held by the Dealer class)

class Player:

    def __init__(self):
        self.guessed_letters = []

    def get_guess(self, guess):

    # takes an input of a letter
    # ensures it is a letter by checking it against a list of the alphabet
    # returns valid letter: guess

        guess = 0
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                    "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        while guess not in alphabet:
            guess = input("What is your guess: ")
            if guess.isdigit() == True:
                print("That is a number, please choose a letter :)")
            elif len(guess) != 1:
                print("That is too long, only one letter accepted per guess")
            elif guess in self.guessed_letters:
                print(f"You have already guessed {guess} before")
            else:
                self.guessed_letters.append(guess)
                print("Thank you, you have not guessed that before")
        return guess
        pass

    def check_guess(self):
        pass

# me = Player()
# me.get_guess()
# print(me.guessed_letters)