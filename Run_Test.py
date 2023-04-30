import random
import numpy as np

arr = []
arr2 = []

# for player's card
card_values = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
random_value = random.choice(card_values)
random_suit = random.choice(card_suits)
random_card = (random_value, random_suit)
for i in random_card:
    print(random_card)

# for dealer's card
card_val = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_s = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
random_val = random.choice(card_val)
random_s = random.choice(card_s)
random_c = (random_val, random_s)
for i in random_c:
    print(random_c)

print("Player's card is : ", random_card, "\n"
                                          "Dealer's card is : ", random_c)

if random_value == random_val:
    print("The game has ended in a WAR!!!!")
elif random_value > random_val:
    print("Player is the WINNER!!!")
elif random_value < random_val:
    print("Dealer is the WINNER!!!")
