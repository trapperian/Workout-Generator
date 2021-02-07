#! python3
# deck of cards worout generator
# will eventually take input of four exercises by user
# default 4 if no input are: pushup, squat, lunge, single leg deadlift
# bonus jokers are 100 jumping jacks ;)
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        pass

# deck of cards as classes to add/pop off etc to work down whole deck.
# upon starting deck of cards generator will start
# asks for 4 exercises by user
# each card has assigned rep count
card = Card('spade', 5)
card.show()

