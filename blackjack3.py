import random

class Cards:
    MARKS = ["♦️", "❤️", "♣️", "♠️"]
    
    def __init__(self):
        self.trump = []
        for mark in self.MARKS:
            for i in range(1, 14):  # 1から13までのカードを作成
                self.trump.append((i, mark))
    
    def showcard(self):
        return self.trump

class Blackjack:
    def __init__(self):
        self.cards = Cards()
    
    def cardnum(self):
        print("呼び出し")
    
    def drawcard(self):
        card = random.choice(self.cards.trump)
        print(card)
        if card[0] == 1:  # Assuming 1 represents Ace
            print("エース")
        return card

# Usage
blackjack_game = Blackjack()
drawn_card = blackjack_game.drawcard()