# Binary-Search-Tree
Lab assignment from Python course practicing implementation and application of the BST with duplicate values.

In this lab, you’ll have the opportunity to practice:
+ Defining classes in Python
+ Overloading the ==, <, and > operators in a Python class
+ Implementing and applying the Binary Search Tree (BST) data structure with duplicate values
+ Writing functions that ensure Card objects are in sorted order
+ Testing your functionality with pytest


Introduction
The goal for this lab is to write a program that will manage cards for a card game. All cards have a suit and a rank, which can be used to determine the value of cards in relation to each other. All cards will be managed by a Binary Search Tree (BST) where the best card is the maximum and the worst card is the minimum.

In order to manage cards for this lab, you will define a Card and PlayerHand classes that organizes the cards in a BST data structure.

You will also write pytests in testFile.py illustrating your behavior works correctly.

Card.py
The Card.py file will contain the definition of a Card class. The Card class will hold information about the cards (suit and rank), and for simplicity, it will also double as a node in our PlayerHand BST. We will define the Card attributes as follows:
suit - string value that distinguishes what suit that card is: C (club), D (diamond), H (heart), or S (spade)
rank - string value to distinguish the rank of the card (in ascending value): A (ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J (Jack), Q (Queen), K (King). Assume there is no Joker
parent - a reference to the parent node of a card in the BST, None if it has no parent (it is the root)
left - a reference to the left child of a card in the BST, None if it has no left child
right - a reference to the right child of a card in the BST, None if it has no right child
count - an integer representing the amount of times this card appears in the BST. 1 by default, but it can be greater since your implementation should support duplicate cards


You will write a constructor that allows the user to construct a Card object by passing in values for the suit and rank. Your constructor should also create the count attribute and initialize it to 1, as well as create the parent, left, and right attributes initialized to None.
__init__(self, suit, rank)

Your Card class definition should also support “getter” and “setter” methods.

Lastly, your Card class can overload the >, <, and == operators. This is optional, but it can be helpful when inserting cards into their proper position within the PlayerHand BST. In this context, a Card should first be compared by its rank. For our purposes, we treat A (Ace) as the smallest, and K (King) as the largest. If the rank is equal, we then compare the suit of the cards, where C (Club) < D (Diamond) < H (Heart) < S (Spade). By this logic, == should only return True if both the suit and the rank are equal. Note: you should also make sure that you handle the suit and rank of your Card case-insensitively, meaning that Card('s', 'a'), Card('S', 'A'), or Card('s', 'A') are all valid inputs and should be handled as the same card.




PlayerHand.py
The PlayerHand.py file will contain the definition of a PlayerHand class. This will keep track of the cards a player has in their hand, implemented as a BST. The PlayerHand will manage Card objects based on their suit and rank.

__init__(self) - the constructor for the PlayerHand will simply initialize the empty BST.


In addition to the construction of the BST in this class, the following methods are required to be implemented:
getTotalCards(self) - returns the total number of cards in hand
getMin(self) - returns the card with the lowest value from the player’s hand. Returns None if there is no card in the hand
getSuccessor(self, suit, rank) - attempts to finds the Card with the suit and rank, and returns the card with the next greatest value. Returns None if there is no card with the specified suit and rank, or if the Card is the maximum and has no successor. Note, this includes any successor of the Card if it exists, not just the successor used for BST maintenance.
put(self, suit, rank) - this adds a card with the specified suit and rank to the BST. If that Card already exists in the BST, increment the count for that Card
delete(self, suit, rank) - attempts to find the Card with the specified suit and rank, and decrements the Card count. If the count is 0 after decrementing the count, remove the node from the BST entirely. Returns True if the Card was successfully removed or decremented, and False if the card is not present in the BST
isEmpty(self) - returns True if there are no cards in the BST and returns False otherwise
get(self, suit, rank) - attempts to find the Card with the specified suit and rank, and returns the Card object if it exists. Otherwise, return None
inOrder(self) - returns a string with the in-order traversal of the BST. Printing the in-order traversal should help check that the cards are in the correct order in the tree
preOrder(self) - returns a string with the pre-order traversal of the BST. BSTs with the same structure should always have the same pre-order traversal, so this can be used to verify that everything was inserted correctly



testFile.py
This file should test all of your classes using pytest. Think of various scenarios and edge cases when testing your code according to the given descriptions. You should test every class’ method functionality (except for getters / setters).
