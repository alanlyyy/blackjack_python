"""
05-27-2020 
Added:
self.hand_score for compute total rank of hand for each round 
add_to_purse()
get_purse()
add_bet()
reset_bet()
reset_hand_score()
set_hand_score()
get_hand_score()
"""
class Player:
    
    def __init__(self,purse):
        
        #stores Card objects
        self.hand = []
        
        #stores current bet
        self.bet = 0
        
        #stores current purse
        self.purse = purse
        
        self.hand_score = 0
    
    def reset_hand(self):
        """reset hand"""
        self.hand = []
    
    def draw_card(self,card):
        """draw card to hand."""
        self.hand.append(card)
    
    def get_hand(self):
        return self.hand
        
    def get_current_bet(self):
        return self.bet
    
    def add_to_purse(self,earnings):
        self.purse += earnings
        return self.purse
    
    def get_purse(self):
        return self.purse
    
    def add_bet(self,bet):
        """User adds bet to existing bet for each game"""
        
        #subtract bet from the purse
        self.purse -= bet
        
        #add bet to existing bet
        self.bet += bet
        
        return self.bet
    
    def reset_bet(self):
        
        self.bet = 0
        
        return self.bet
    
    def reset_hand_score(self):
        self.hand_score = 0
        return set_hand_score
    
    def set_hand_score(self,score):
        self.hand_score = score
    
    def get_hand_score(self):
        return self.hand_score
        
    