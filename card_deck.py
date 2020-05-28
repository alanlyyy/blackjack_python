"""Implemented Deck Class and Card Class. 05-25-20
Passed test.

"""
from random import shuffle

class Deck:
    
    def __init__(self):
        self.suits = ["D", "C", "H", "S"]
        self.values = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]
        self.deck = []
        
    def create_deck(self):
        """
        Create a deck of 52 cards.
        """
        for value in self.values:
            
            for suit in self.suits:
                
                self.deck.append( Card(value,suit) )
        
        return self.deck
    
    def shuffle_deck(self):
        shuffle(self.deck)
        return self.deck
        
    def deal_card(self):
        return self.deck.pop()
        
    def reset_deck(self):
        #create deck and shuffle the card objects
        self.deck = []
        self.create_deck() 
        self.shuffle_deck()
        return self.deck
    
    def deck_len(self):
        return len(self.deck)
    
    def get_deck(self):
        return self.deck

class Card(Deck):
    """Container used to store suit and value
    """
    
    def __init__(self,value,suit):
        
        self.suit = suit
        self.value = value
    
    def get_card(self):
        return ("Suit: ", self.suit, "Value: ", self.value)
        
if __name__ == "__main__":
    
    test_deck = Deck()
    print(test_deck.create_deck())
    test_deck.shuffle_deck()
    
    #pop card 1
    popped_card = test_deck.deal_card()
    print(test_deck.deck_len())
    
    print("CARD VALUE: " , popped_card.value, "CARD_SUIT: ", popped_card.suit)
    
    #pop card 2
    popped_card = test_deck.deal_card()
    print("CARD VALUE: " , popped_card.value, "CARD_SUIT: ", popped_card.suit)
    
    #create a new shuffled deck
    print(test_deck.reset_deck())
    
    #pop card 3
    popped_card = test_deck.deal_card()
    
    #test card class
    test_card = Card( popped_card.value, popped_card.suit)
    
    #print Card and suit
    print(test_card.suit, test_card.value)
    
    print(test_card.get_card())
    
    
    #pop card 4
    popped_card = test_deck.deal_card()
    
    test_card2 = Card(popped_card.value, popped_card.suit)
    print(test_card2.get_card())
    
    print("length: ", test_deck.deck_len())