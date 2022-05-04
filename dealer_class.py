# class which knows the word
# keeps tabs on letters guessed and which are correct

class Dealer:

    def __init__(self):
        self.mystery_word = ""
        pass

    def set_mystery_word(self):
        while self.mystery_word == "":
            self.mystery_word = input("Dealer: please type in the mystery word: ")

    def get_mystery_word(self):
        return self.mystery_word