# PlayerHand.py

from Card import Card

class PlayerHand:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def getTotalCards(self):
        return self.size
    
    def getMin(self):
        if self.root:
            current = self.root
            while current.getLeft():
                current = current.left
            return current.__str__()
        else:
            return None
    
    def getSuccessor(self, suit, rank):
        suit = suit.upper()
        if rank.isnumeric():
            rank = rank
        else:
            rank = rank.upper()
        if self.size > 1:
            cc = self._get(suit,rank,self.root)
            if cc:
                succ = cc.findSuccessor()
                return succ.__str__()
            else:
                return None
        else:
            return None
    
    def put(self, suit, rank):
        suit = suit.upper()
        if rank.isnumeric():
            rank = rank
        else:
            rank = rank.upper()
        if self.root:
            self._put(suit, rank, self.root)
        else:
            self.root = Card(suit, rank)
        self.size += 1
        
    def _put(self, suit, rank, currentCard):
        if Card(suit, rank) < currentCard:
            if currentCard.getLeft():
                self._put(suit, rank, currentCard.left)
            else:
                currentCard.left = Card(suit, rank)
                currentCard.left.parent = currentCard
        elif Card(suit, rank) == currentCard:
            currentCard.count += 1
        else:
            if currentCard.getRight():
                self._put(suit, rank, currentCard.right)
            else:
                currentCard.right = Card(suit, rank)
                currentCard.right.parent = currentCard
        
    def delete(self, suit, rank):
        suit = suit.upper()
        if rank.isnumeric():
            rank = rank
        else:
            rank = rank.upper()
        if self.size > 1:
            cardToRemove = self._get(suit,rank,self.root)
            if cardToRemove: 
                if cardToRemove.count > 1:
                    cardToRemove.count = cardToRemove.count - 1
                    self.size = self.size - 1
                    return True
                else:
                    self.remove(cardToRemove)
                    self.size = self.size - 1
                    return True
            else:
                return False
        elif self.size == 1 and self.root == Card(suit,rank):
            self.root = None
            self.size = self.size - 1
            return True
        else:
            return False
        
    def remove(self,currentCard):
        if currentCard.isLeaf():
            if currentCard == currentCard.parent.left:
                currentCard.parent.left = None
            else:
                currentCard.parent.right = None
        elif currentCard.hasBothChildren():
            succ = currentCard.findSuccessor()
            succ.spliceOut()
            currentCard.suit = succ.suit.upper()
            if succ.rank.isnumeric():
                currentCard.rank = succ.rank
            else:
                currentCard.rank = succ.rank.upper()
            currentCard.count = succ.count
            
        else:
            if currentCard.getLeft():
                if currentCard.isLeftChild():
                    currentCard.left.parent = currentCard.parent
                    currentCard.parent.left = currentCard.left
                elif currentCard.isRightChild():
                    currentCard.left.parent = currentCard.parent
                    currentCard.parent.right = currentCard.left
                else:
                    currentCard.replaceCardData(currentCard.left.suit,
                        currentCard.left.rank, currentCard.left.count,
                        currentCard.left.left,
                        currentCard.left.right)
            else:
                if currentCard.isLeftChild():
                    currentCard.right.parent = currentCard.parent
                    currentCard.parent.left = currentCard.right
                elif currentCard.isRightChild():
                    currentCard.right.parent = currentCard.parent
                    currentCard.parent.right = currentCard.right
                else:
                    currentCard.replaceCardData(currentCard.right.suit,
                        currentCard.right.rank, currentCard.right.count,
                        currentCard.right.left,
                        currentCard.right.right)        
    
    
    def isEmpty(self):
        return self.size == 0
    
    def get(self, suit, rank):
        suit = suit.upper()
        if rank.isnumeric():
            rank = rank
        else:
            rank = rank.upper()
        if self.root:
            res = self._get(suit,rank,self.root)
            if res:
                return res.__str__()
            else:
                return None
        else:
            return None
        
    def _get(self,suit,rank,currentCard):
        if not currentCard:
            return None
        elif currentCard == Card(suit, rank):
            return currentCard
        elif Card(suit, rank) < currentCard:
            return self._get(suit,rank,currentCard.left)
        else:
            return self._get(suit,rank,currentCard.right)
    

    def inOrder(self):
        card = self.root
        return self._inOrder(card)

    def _inOrder(self, card):
        ret = ""
        if card != None:
            ret += self._inOrder(card.left)
            ret += card.__str__()
            ret += self._inOrder(card.right)
        return ret
    
    def preOrder(self):
        card = self.root
        return self._preOrder(card) 
    
    def _preOrder(self, card):
        ret = ""
        if card != None:
            ret += card.__str__()
            ret += self._preOrder(card.left)
            ret += self._preOrder(card.right)
        return ret
