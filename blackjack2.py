import random
class Card:
    MARKS = ["♦️", "❤️", "♣️", "♠️"]
    def __init__(self):
        self.trump = []
        for mark in self.MARKS:
            for i in range(1, 14):  # 1から13までのカードを作成
                self.trump.append((i, mark))
    def showcard(self):
        return self.trump

# カードの作成と表示
my_card = Card()
Cards = my_card.showcard()

print(random.choice(Cards))