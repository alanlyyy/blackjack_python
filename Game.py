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
                print("Computer Loss: ",player_score, cpu_score, self.Computer.get_current_bet())
                
                #add to Players purse
                self.Player.add_to_purse(self.Computer.get_current_bet())
            
            else:
                print("Player 1 Loss: ",player_score, cpu_score, self.Player.get_current_bet())
                
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
        
        ace = " "
        
        for card in list_of_cards:
            
            #get value of card
            current_card = card.get_card()[3]
            
            #check if adding an ace makes the player bust
            if current_card == 'A':
                
                if hand_score + 11 < 22:
                    
                    hand_score += 11
                    
                    #skip everything else in the loop
                    continue 
            
            #this case looks at all face cards including A, A is treated as 1
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

def test():
    """
    1.Test integration of deck class into game class.
    2. Test facecard_to_int function
    3. Test calc_hand_score function.
    """
    
    new_game = blackjack_game(50)
    
    print("Actual: ", new_game.facecard_to_int("K"), "Expected: ", 10)
    print("Actual: ", new_game.facecard_to_int("A"), "Expected: ", 1)
    
    #create and shuffle deck
    new_game.game_deck.create_deck()
    new_game.game_deck.shuffle_deck()
    
    hand = [ new_game.game_deck.deal_card(), new_game.game_deck.deal_card()]
    
    print("Actual: ", new_game.game_deck.deck_len(),"Expected: ", 50)
    print("Current_Hand: ", hand[0].get_card()[3], hand[1].get_card()[3])
    
    print("Hand Score: ", new_game.calc_hand_score(hand))

def test2():
    """
    Test calculate handscore class.
    """
    
    new_game = blackjack_game(50)
    
    #create and shuffle deck
    new_game.game_deck.create_deck()
    new_game.game_deck.shuffle_deck()
    
    new_game.Player.set_hand(new_game.game_deck.deal_card())
    new_game.Player.set_hand(new_game.game_deck.deal_card())
    
    p1_hand = new_game.Player.get_hand()
    
    print("Player Hand: ", p1_hand[0].get_card()[3], p1_hand[1].get_card()[3])

    new_game.Computer.set_hand(new_game.game_deck.deal_card())
    new_game.Computer.set_hand(new_game.game_deck.deal_card())
    
    c_hand = new_game.Computer.get_hand()
    
    print("Computer Hand: ", c_hand[0].get_card()[3], c_hand[1].get_card()[3])
    
    #calculate hand score and set hand score in player object
    new_game.Player.set_hand_score(new_game.calc_hand_score(p1_hand))
    
    #calculate hand score and set hand score in computer object   
    new_game.Computer.set_hand_score(new_game.calc_hand_score(c_hand))
    
    #determine the new winner
    new_game.calc_winner_round()

if __name__ == "__main__":
    test()
    print("----")
    test2()
    