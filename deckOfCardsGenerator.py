#! python3
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
# deck of cards workout generator
# deck of cards as classes to add/pop off etc to work down whole deck.
# upon starting deck of cards generator will start
# asks for 4 exercises by user
# each card has assigned rep count


