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
        self.playersum = 0
        self.playercard = []

    def cardnum(self, card):
        self.playercard.append(card)
        self.playersum += min(card[0], 10)  # 10, J, Q, Kは10として扱う
        print(self.playercard, self.playersum)

    def drawcard(self):
        card = random.choice(self.cards.trump)
        self.cards.trump.remove(card)  # 引いたカードをデッキから削除
        return card

# Usage
blackjack = Blackjack()
for i in range(3):  # デバッグ
    drawCard = blackjack.drawcard()
    blackjack.cardnum(drawCard)