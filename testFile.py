# testFile.py

from Card import Card
from PlayerHand import PlayerHand

# testing Card.py 

def test___str__():
    c = Card("d",'A')
    assert c.__str__() == 'D A | 1\n'
    
def test_isLeftChild():
    c = Card("d",'A')
    assert c.isLeftChild() == None
    
def test_isRightChild():
    c = Card("d",'A')
    assert c.isRightChild() == None
    
def test_isLeaf():
    c = Card("d",'A')
    assert c.isLeaf() == True
    
def test_hadAnyChildren():
    c = Card("d",'A')
    assert c.hasAnyChildren() == None
    
def test_hasBothChildren():
    c = Card("d",'A')
    assert c.hasBothChildren() == None
    
def test_replaceCardData():
    c = Card("d",'A')
    c.replaceCardData('h','5',1,None,None)
    assert c.__str__() == 'h 5 | 1\n'
    
def test_findMin():
    c = Card("d",'A')
    assert c.findMin().__str__() == 'D A | 1\n'
    
def test_findSuccessor():
    c = Card("d",'A')
    assert c.findSuccessor() == None
    
def test_spliceOut():
    c1 = Card("d",'A')
    c2 = Card("S",'K')
    c1.setParent(c2)
    assert c2.left == c1
    c1.spliceOut()
    assert c2.left == None
    
def test_gt():
    c1 = Card("d",'A')
    c2 = Card("S",'K')
    assert (c2 > c1) == True
    
def test_lt():
    c1 = Card("d",'A')
    c2 = Card("S",'K')
    assert (c1 < c2) == True
    
def test_eq():
    c1 = Card("d",'a')
    c2 = Card("D",'A')
    assert (c1 == c2) == True
    
def test_ne():
    c1 = Card("d",'a')
    c2 = Card("S",'K')
    assert (c1 != c2) == True


# tesing PlayerHand.py

def test_getTotalCards():
    h = PlayerHand()
    assert h.getTotalCards() == 0
    h.put("d","K")
    assert h.getTotalCards() == 1
    assert h.delete("D","k") == True
    assert h.getTotalCards() == 0
    h.put("d","K")
    h.put("d","K")
    h.put("d","K")
    assert h.getTotalCards() == 3
        
def test_getMin():
    h = PlayerHand()
    assert h.getMin() == None
    h.put("c","5")
    assert h.getMin() == 'C 5 | 1\n'
    h.put("d","J")
    h.put("c","4")
    assert h.getMin() == 'C 4 | 1\n'
    h.put("d","4")
    assert h.getMin() == 'C 4 | 1\n'
    h.put("H","A")
    h.put("H","a")
    assert h.getMin() == 'H A | 2\n'
        
def test_getSuccessor():
    h = PlayerHand()
    assert h.getSuccessor("C", "5") == None
    h.put("c","5")
    h.put("d","J")
    h.put("c","4")
    h.put("d","4")
    h.put("H","A")
    h.put("H","a")
    assert h.getSuccessor("H", "A") == 'C 4 | 1\n'
    assert h.getSuccessor("d", "4") == 'C 5 | 1\n'
    assert h.getSuccessor("c", "4") == 'D 4 | 1\n'
    assert h.getSuccessor("c", "5") == 'D J | 1\n'
    assert h.getSuccessor("d", "j") == 'None'
        
def test_put():
    h = PlayerHand()
    assert h.getTotalCards() == 0
    h.put("H","a")
    assert h.getTotalCards() == 1
    assert h.getMin() == 'H A | 1\n'
    h.put("h","A")
    h.put("h","a")
    h.put("H","A")
    assert h.getMin() == 'H A | 4\n'
    assert h.getTotalCards() == 4
        
def test_delete():
    h = PlayerHand()
    assert h.delete("d","k") == False
    h.put("d","k")
    h.put("d","k")
    assert h.getMin() == 'D K | 2\n'
    assert h.delete("d","k") == True
    assert h.getMin() == 'D K | 1\n'
    assert h.delete("d","k") == True
    assert h.getMin() == None
    assert h.getTotalCards() == 0
        
def test_isEmpty():
    h = PlayerHand()
    h.put("d","k")
    assert h.isEmpty() == False
    assert h.delete("d","k") == True
    assert h.isEmpty() == True
        
def test_get():
    h = PlayerHand()
    assert h.get("D","K") == None
    h.put("d","k")
    assert h.get("D","K") == 'D K | 1\n'
    h.put("d","k")
    assert h.get("D","K") == 'D K | 2\n'
    assert h.delete("d","k") == True
    assert h.get("D","K") == 'D K | 1\n'
    assert h.delete("d","k") == True
    assert h.delete("d","k") == False
    assert h.get("D","K") == None
        
def test_inOrder():
    h = PlayerHand()
    h.put("c","5")
    h.put("d","J")
    h.put("H","A")
    h.put("c","4")
    h.put("d","4")
    h.put("H","a")
    assert h.inOrder() == \
    'H A | 2\nC 4 | 1\nD 4 | 1\nC 5 | 1\nD J | 1\n'
        
        
def test_preOrder():
    h = PlayerHand()
    h.put("c","5")
    h.put("d","J")
    h.put("H","A")
    h.put("c","4")
    h.put("d","4")
    h.put("H","a")
    assert h.preOrder() == \
    'C 5 | 1\nH A | 2\nC 4 | 1\nD 4 | 1\nD J | 1\n'
