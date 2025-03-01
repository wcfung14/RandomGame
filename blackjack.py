import random

class Hand:
    def __init__(self, deck):
        self.hand = []
        self.card_conversion = {"A": 1, "J": 10, "Q": 10, "K": 10, }
        self.val = 0
        for _ in range(2):
            self.draw(deck)
    
    def draw(self, deck):
        card = random.choice(deck)
        deck.remove(card)
        self.hand.append(card)
    
    def cheat(self, card_to_cheat: list):
        self.hand = card_to_cheat
    
    def check(self):
        self.val = 0
        A_count = 0
        for i in self.hand:
            if i[1:] == "A":
                A_count += 1

            elif i[1:] in ["J", "Q", "K"]:
                self.val += self.card_conversion[i[1:]]
            else:
                self.val += int(i[1:])
        
        for _ in range(A_count):
            if self.val + 11 > 21:
                self.val += 1
            else:
                self.val += 11

        if len(self.hand) == 2 and self.val == 21:
            return "Black Jack"
        else:
            return self.val


def game():
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    kinds = ["♣", "♦", "♥", "♠"]
    deck = [i+str(j) for j in cards for i in kinds]

    player = Hand(deck = deck)
    dealer = Hand(deck = deck)

    while True:
        print(f"player: {player.hand}")
        print(player.check())
        print(f"dealer: {dealer.hand}")
        print(dealer.check())

        if player.check() == dealer.check() and (dealer.check() == 21 or dealer.check() == "Black Jack"):
            return "Draw - Eat stick"
        elif player.check () == "Black Jack":
            return "Black Jack - Player win!"
        elif dealer.check () == "Black Jack":
            return "Black Jack - Dealer win!"
        elif player.check() > 21:            
            return "Player Busted"
        elif dealer.check() > 21:
            return "Dealer Busted"
        else:
            ask = input("Draw another card?").lower()
            if ask == "yes":
                player.draw(deck)
            elif ask == "no":
                while dealer.check() < player.check():
                    dealer.draw(deck)
                
    if player.check() == dealer.check():
        return "Draw"
    elif player.check() > dealer.check():
        return "Player win!"
    elif player.check() < dealer.check():
        return "Dealer win!"


result = game()
print(result)


# player.cheat(["♣A", "♦A", "♥A", "♠A"])
# print(player.check())