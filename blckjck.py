import random

def createDeck():
        deck = []
        suit = ["h","s","c","d"]
        card = []
        for x in range(len(suit)):
                for y in range(0,14):
                        card = [suit[x],y]
                        deck.append(card)
        return deck
        
def shuffle(deck):
        random.shuffle(deck)
        return deck

def play(deck):
        score = 0
        play = True
        x = 1
        while play == True:
                newCard = drawCard(deck, x)
                score = score + newCard
                print score
                x = x + 1
                if score > 21:
                        print "out too high!"
                        break
                elif score == 21:
                        print "blackjack bitch"
                        break
                hs = raw_input("hit or stay")
                if hs == "h":
                        print "Hit Me!"
                elif hs == "s":
                        #print "stay"
                        print "Final Score:", score
                        break
def drawCard(deck, x):
        card = deck[x]
        print "Card Drawn:",card[1]
        if card[1] > 10:
            newCard = 10
        else:
            newCard = card[1]
        return newCard

def main():
    print "Welcome to Blackjack!"
    cont = True
    while cont == True:
        play(shuffle(createDeck()))
        again = raw_input("Play again? [y/n]")
        if again == "n":
            print "Exiting Game"
            break
        
if __name__ == "__main__":
    main()
