# Card.py

class Card:
    def __init__(self, suit, rank):
        self.suit = suit.upper()
       
        if rank.isnumeric():
            self.rank = rank
        else:
            self.rank = rank.upper()
        
        self.count = 1
        self.parent = None
        self.left = None
        self.right = None
        
        
    def getSuit(self):
        return self.suit
    
    def setSuit(self, suit):
        self.suit = suit.upper()
        
    def getRank(self):
        return self.rank
    
    def setRank(self, rank):
        if rank.isnumeric():
            self.rank = rank
        else:
            self.rank = rank.upper()
            
    def getCount(self):
        return self.count
    
    def setCount(self, count):
        self.count = count
        
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent
        if self.getParent():
            if self > self.parent:
                self.parent.right = self
            elif self == self.parent:
                self.parent.right = self
            else:
                self.parent.left = self
        
    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left
        if self.getLeft():
            self.left.parent = self
        
    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right
        if self.getRight():
            self.right.parent = self
    
    def isLeftChild(self):
        return self.parent and self.parent.left == self
    
    def isRightChild(self):
        return self.parent and self.parent.right == self
    
    def isLeaf(self):
        return not (self.right or self.left)
    
    def hasAnyChildren(self):
        return self.right or self.left
    
    def hasBothChildren(self):
        return self.right and self.left
    
    def replaceCardData(self, suit, rank, count, lc, rc):
        self.suit = suit
        self.rank = rank
        self.count = count
        self.left = lc
        self.right = rc
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self
    
    def findMin(self):
        current = self
        while current.getLeft():
            current = current.left
        return current
    
    def findSuccessor(self):
        succ = None
        if self.getRight():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    self.parent.right = self
        return succ
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.getLeft():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
    
    def __str__(self):
        return "{} {} | {}\n".format(self.suit, self.rank, self.count)
    
    def __gt__(self,rhs):
        suits = {"C":1, "D":2, "H":3, "S": 4}
        ranks = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
        if ranks.get(self.rank) == ranks.get(rhs.rank):
            return suits.get(self.suit) > suits.get(rhs.suit)
        else:
            return ranks.get(self.rank) > ranks.get(rhs.rank)
        
    def __lt__(self,rhs):
        suits = {"C":1, "D":2, "H":3, "S": 4}
        ranks = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
        if ranks.get(self.rank) == ranks.get(rhs.rank):
            return suits.get(self.suit) < suits.get(rhs.suit)
        else:
            return ranks.get(self.rank) < ranks.get(rhs.rank)
        
    def __eq__(self,rhs):
        suits = {"C":1, "D":2, "H":3, "S": 4}
        ranks = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
        if self is None or rhs is None:
            return False
        else:
            return ranks.get(self.rank) == ranks.get(rhs.rank) and \
                suits.get(self.suit) == suits.get(rhs.suit)
    
    def __ne__(self,rhs):
        suits = {"C":1, "D":2, "H":3, "S": 4}
        ranks = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
        return self.suit != None
