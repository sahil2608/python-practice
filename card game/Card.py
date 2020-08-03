from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "club"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.card = None


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15): # Card created and shuffled
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self): # card taken out
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Game:
    def __init__(self):
        name1 = input("Enter your name p1")
        name2 = input("Enter your name p2")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print("{} Wins this round".format(winner))

    def draw(self, p1n, p1c, p2n, p2c):
        print("{} drew {} {} drew {}".format(p1n, p1c, p2n, p2c))

    def play_game(self): #starting point of program
        cards = self.deck.cards
        print('Begin The Game!')
        while len(cards) >= 2:
            response = input("Press q to quit, press any key to continue")
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p1.wins += 1
                self.wins(self.p1.name)

            win = self.winner(self.p1, self.p2)
            print("Game is Over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return  p2.name
        else:
            return "It is a tie"


game = Game()
game.play_game()