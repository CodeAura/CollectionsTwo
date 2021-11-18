import itertools
import random

Kaarten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Aas', 'Heer', 'Joker']
Kleuren = ['Klaveren', 'Schoppen', 'Harten', 'Ruiten']

deck = list(itertools.product(Kaarten, Kleuren))

random.shuffle(deck)

for i in range(7):
    i += 1
    print('Kaart ' + str(i) + ': ' + str(deck[i]))
    
print('Deck: ' + '(Aantal kaarten: ' + (str(len(deck))) + ")")
print(deck)