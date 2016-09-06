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