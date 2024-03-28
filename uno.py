class UNOcard:
    def __init__(self, color, number):
        self.c = color
        self.n = number

    def __str__(self):
        strReturn = ' '.join([self.c, str(self.n)])
        return strReturn

    def canPlay(self, other):
        if (self.c == other.c) or (self.n == other.n):
            return True
        else:
            return False


class CollectionOfUnoCards:

    def __init__(self):
        self.card_list = []
        len(self.card_list)

    def __str__(self):
        strReturn = ""
        for card in self.card_list:
            strReturn = strReturn + str(card) + "; "
        return strReturn

    def addCard(self, card):
        self.card_list.append(card)

    def makeDeck(self):
        self.card_list.clear()
        for number in range(1, 10):
            for color in ['Blue', 'Green', 'Yellow', 'Red']:
                card = UNOcard(color, number)
                self.card_list.append(card)
                self.card_list.append(card)

    def shuffle(self):
        import random
        num_cards = len(self.card_list)
        for counter in range(200):
            for i in range(num_cards):
                j = random.randrange(i, num_cards)
                self.card_list[i], self.card_list[j] = self.card_list[j], self.card_list[i]

    def getNumCards(self):
        return len(self.card_list)

    def getTopCard(self):
        return self.card_list[0]

    def canPlay(self, c):
        for card in self.card_list:
            if (card.canPlay(c)):
                return self.card_list.index(card)
            else:
                continue
        return -1

    def getCard(self, index):
        return self.card_list.pop(index)


class Uno:


    def __init__(self):
        self.deck = CollectionOfUnoCards()
        self.deck.makeDeck()
        self.deck.shuffle()

        print("Initial Number of cards in deck: " + str(self.deck.getNumCards()))

        self.discardPile = CollectionOfUnoCards()

        self.lastPlayedCard = UNOcard(0, 1)

        self.hand1 = CollectionOfUnoCards()
        self.hand2 = CollectionOfUnoCards()

        self.dealHands()
        self.result = ''

        print("Player-1 Hand: " + str(self.hand1))
        print("Player-2 Hand: " + str(self.hand2))

        print("Number of cards left in deck after first deal: " + str(self.deck.getNumCards()))

    def __str__(self):
        return super().__str__()

    def dealHands(self):
        import random
        for i in range(7):
            cardIndex = random.randrange(0, self.deck.getNumCards())
            self.hand1.addCard(self.deck.getCard(cardIndex))

            cardIndex = random.randrange(0, self.deck.getNumCards())
            self.hand2.addCard(self.deck.getCard(cardIndex))


    def playGame(self):

        import random
        randomIndex = random.randrange(0, self.hand1.getNumCards())
        firstCardEverPlayed = self.hand1.getCard(randomIndex)
        self.lastPlayedCard = firstCardEverPlayed


        while (True):
            self.playTurn(self.hand2)
            if self.hand2.getNumCards() == 0:
                self.result = "player2 is winner"
                return
            
            self.playTurn(self.hand1)
            if self.hand1.getNumCards() == 0: 
                self.result = "Player1 is winner"
                return

            if self.deck.getNumCards() == 0:
                self.result = "This is a tie"
                return
            

    def playTurn(self, player):
        canIPlay = player.canPlay(self.lastPlayedCard)
        if canIPlay != -1:
            self.lastPlayedCard = player.getCard(canIPlay)
        else:
            player.addCard(self.deck.getCard(self.deck.getNumCards()-1))
        
    
    def printResult(self):
        print(self.result)

    def main(self):
        self.playGame()
        self.printResult()

u = Uno()
u.main()
