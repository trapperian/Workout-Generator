#! python3
# deck of cards worout generator
# will eventually take input of four exercises by user
# default 4 if no input are: pushup, squat, lunge, single leg deadlift
# bonus jokers are jumping jacks, high knees, burpees and mountain climbers ;)
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for v in range(1, 15):
                self.cards.append(Card(suit, v))

    def show(self):
        for card in self.cards:
            card.show()

deck = Deck()
deck.show()

# deck of cards as classes to add/pop off etc to work down whole deck.
# upon starting deck of cards generator will start
# asks for 4 exercises by user
# each card has assigned rep count


