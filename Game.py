"""
05-27-2020
Implemented 
calc_winner_round: to determine winner per each round
calc_hand_score: to calculate the rank of the hand per each round.
facecard_to_int: converts facecards to numeric value
self.Player and self.Computer: player and computer objects

Player class and blackjack_game class have not been tested yet.
"""

from card_deck import Deck
from players import Player

class blackjack_game:
    
    def __init__(self,purse):
        
        #store the new deck
        self.game_deck = Deck()
        
        #initialize player with a purse
        self.Player = Player(purse)
        
        #initialize computer player with a purse
        self.Computer = Player(purse)
    
    def play_game(self):
        """
        function used to implement game play.
        """
        #create deck
        self.game_deck.create_deck()
        
        #shuffle deck
        self.game_deck.shuffle_deck()
        
        
        pass
    
    def calc_winner_round(self):
        """
        Determine the winner for each round.
        """
        player_score = self.Player.get_hand_score()
        cpu_score = self.Computer.get_hand_score()
        
        if player_score > 21:
            
            print("Player 1 Loss: ", self.Player.get_current_bet())
            
            #add to Players purse
            self.Computer.add_to_purse(self.Player.get_current_bet())
            
        elif cpu_score > 21:
            
            print("Computer Loss: ", self.Player.get_current_bet())
            
            #add to Players purse
            self.Player.add_to_purse(self.Computer.get_current_bet())
        
        #if player and cpu does not bankrupt
        else:
            
            if player_score > cpu_score:
                print("Computer Loss: ", self.Player.get_current_bet())
                
                #add to Players purse
                self.Player.add_to_purse(self.Computer.get_current_bet())
            
            else:
                print("Player 1 Loss: ", self.Player.get_current_bet())
                
                #add to Players purse
                self.Computer.add_to_purse(self.Player.get_current_bet())
                
        #reset bet for new round
        self.Player.reset_bet()
        self.Computer.reset_bet()
        
        #reset hand for new round
        self.Player.reset_hand()
        self.Computer.reset_hand()
        
    def calc_hand_score(self, list_of_cards):
        
        hand_score = 0
        
        for card in list_of_cards:
            
            #get value of card
            current_card = card.get_card()[3]
            
            if type(current_card) == str:
                #convert K,Q,J,A
                hand_score += self.facecard_to_int(current_card)
            else:
                hand_score += current_card
        
        return hand_score
   
    def facecard_to_int(self, current_card):
        
        face_cards = {
                        "K":10, "Q":10, "J":10, "A":1
                    }
        try:
        
            #if K,Q,J or A
            return face_cards.get(current_card)
        
        except:
        
            #if numeric card
            return current_card
        