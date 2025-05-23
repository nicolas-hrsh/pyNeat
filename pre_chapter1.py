# These are exercises required for chapter 1
'''
Problem 1: Create a Simple Card Object Using a Class
📌 Goal: Understand how to define a class and create an object.

Instructions:
Create a class Card with two attributes: rank and suit.
Create a card with rank "A" and suit "hearts".
Print both attributes.
 '''
class Card():
    #att
    rank : str
    suit : str

    #behav
    def __init__(self):
        rank = 'blank'
        suit = 'blank'

card = Card()
card.rank = "A"
card.suit = "hearts" 
print(card.rank +' of '+ card.suit)


'''
✅ Problem 2: Make a Full Deck of Cards
📌 Goal: Use a loop and list to store many card objects.

Instructions:
Create all combinations of ranks and suits using a loop.
Store each card as a tuple: ("A", "hearts"), ("2", "hearts"), ..., ("K", "spades").
Store them all in a list called deck.
Bonus: Print the first and last card in the deck.
'''
# Think: Hmm... so we need a container to store stuff. The big container is a list, small containers inside will be tuples. So, lets create inside code first, a loop to generate a tuple the at end append it to a list.
allCards = []
for x in range(2,11):
    for y in ("heart", "diamond", "spade", "club"):
        allCards.append((str(x), y))
for x in ['J','Q','K','A']:
    for y in ("heart", "diamond", "spade", "club"):
        allCards.append((str(x), y))

print(allCards)



'''
 Problem 3: Use namedtuple for Cards
📌 Goal: Learn how to use namedtuple to make objects quickly.

Instructions:

Use from collections import namedtuple to create a Card namedtuple.

Create one card: Card("Q", "diamonds")

Print: Q of diamonds
'''


'''
 Problem 4: Write a FrenchDeck Class (Mini Version)
📌 Goal: Understand how a class can behave like a list.

Instructions:

Create a class FrenchDeck with an internal list of Cards.

Implement two special methods:

__len__ to return the number of cards.

__getitem__ to return a card at a given index.
'''


'''
Problem 5: Pick a Random Card
📌 Goal: Use the random module with your class.

Instructions:

Import random

Use random.choice(deck) to pick a card from your FrenchDeck.
'''


