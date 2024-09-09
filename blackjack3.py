import random
import sys
class Cards:
    marks = ["♦️", "❤️", "♣️", "♠️"]
    # numbers = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.trump = []
        for mark in self.marks:
            for i in range(1, 14):
                self.trump.append((i, mark))

    def showcard(self):
        return self.trump

class Blackjack:
    def __init__(self):
        self.playersum = 0
        self.cards = Cards()
        self.playercard = []

    def cardnum(self, card):
        self.playercard.append(card)
        if card[0] >= 11:
            self.playersum += 10
        elif card[0] == 1:
            if self.playersum + 11 <= 21:
                self.playersum += 11
            else:
                self.playersum += 1
        else:
            self.playersum += int(card[0])
        return self.playercard, self.playersum

    def drawcard(self):
        card = random.choice(self.cards.trump)
        self.cards.trump.remove(card)
        return card
    def checkburst(self,sum):
        if sum>=21:
            print("バースト!")
            print(self.playercard, sum)
            sys.exit()
    def judge(p_sum,d_sum):
        if p_sum > d_sum:
            self.checkburst



blackjack = Blackjack()
for i in range(2):
    drawCard = blackjack.drawcard()
    p_card,p_sum=blackjack.cardnum(drawCard)
    blackjack.checkburst(p_sum)
print(p_card,p_sum)