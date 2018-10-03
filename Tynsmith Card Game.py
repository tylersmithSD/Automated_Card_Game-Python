#Developer: Tyler Smith
#Date:      10.24.16
#Purpose:   The program takes a deck of cards and distributes them between
#           a player and the computer. It displays where all the cards are
#           located and then shows exactly what the computer has in its hand
#           and shows exactly what the player has in their hand.

import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def translateCard(cardNumber):
  suitNum = cardNumber // 13        # Find the number of the cardnumber that corresponds 
  suit    = suitName[suitNum]       # with the correct suit in the list suitName
  rankNum = cardNumber % 13         # Find the number of the cardnumber that corresponds
  rank    = rankName[rankNum]       # with the correct rank of the card in the list rankName
   
  cardName = (rank + ' of ' + suit) # Assign proper cardName and return 
  return cardName                   # value to where function is called

def assignCard(cardRecipient):
  findLoc = True                    # Condition variable for loop
  while(findLoc):                   # Assign player a card by designating a spot in cardLoc
    cardNum = random.randint(0, 51) # Give random card to user
    if(cardLoc[cardNum] == 0):      # Checks to make sure card isn't already delt
      cardLoc[cardNum] = cardRecipient # Assign memory location for player or computer
      findLoc = False               # Leave loop

def showDeck():
  print('       Location of all cards')
  print('#               Card                Location')
  for i in range(52):               # Loop through all of the cards showing where
    if(cardLoc[i] == 0):            # each card is, whether it be in the deck,
      location = 'Deck'             # or in the player's hand or in the 
    elif(cardLoc[i] == 1):          # computer's 'hand'
      location = 'Player'
    elif(cardLoc[i] == 2):
      location = 'Computer'
      
    #Display where every card is to the user
    print ('{} {} {}'.format(i, translateCard(i).rjust(22), location.rjust(18)))

def showHand(cardHolder):
  if(cardHolder == 1):
    print("\nCards in Player's Hand:")       
  elif(cardHolder == 2):
    print("\nCards in Computer's Hand:") 
  for i in range(52):                
    if(cardLoc[i] == cardHolder):        # Loop through all of the cards finding where
      print(translateCard(i))            # the cards are that the function call is asking for
                                         # either the player or user has the card we are looking for
      
def main():
#  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)          

#Run main function
if(__name__ == "__main__"):
  main() 
