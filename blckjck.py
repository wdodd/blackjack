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
		card = deck[x]
		print card
		print card[1]
		score = score + card[1]
		print score
		x = x + 1
		hs = raw_input("hit or stay")
		if hs == "h":
			print "hit"
		elif hs == "s":
			print "stay"
			print score
			break
