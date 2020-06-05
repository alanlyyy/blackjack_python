"""
05-27-2020
Implemented 
calc_winner_round: to determine winner per each round
calc_hand_score: to calculate the rank of the hand per each round.
facecard_to_int: converts facecards to numeric value
self.Player and self.Computer: player and computer objects
Player class and blackjack_game class have not been tested yet.

05-29-2020
1.Implemented test cases for all blackjack_game classes.
2. fixed calc_hand_score function to account for Aces = 11 and Aces = 1

06-04-2020
1. implemented play_game, blackjack_payout, and determine black jack functions
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
    
    def play_game(self,user_ante):
        """
        function used to implement game play.
        """
        
        #flag indicating game has started
        user_play = 1
        
        while ((self.Player.get_purse() > 0) and (self.Computer.get_purse() > 0)) and (user_play != 0):
            
            #create deck
            self.game_deck.create_deck()
            
            #shuffle deck
            self.game_deck.shuffle_deck()
            
            #add bet before game start
            self.Player.add_bet(user_ante)
            self.Computer.add_bet(user_ante)
            
            #deal first 2 card to player and computer
            self.deal_hand_initial(self.Player)
            self.deal_hand_initial(self.Computer)
            
            print("Player: ")
            self.Player.player_show_hand()
            print("CPU: ")
            self.Computer.player_show_hand()
            
            #print current purse and ante
            self.Player.player_stats()
            self.Computer.player_stats()
            
            #determine if we have a black jack winner
            if self.blackjack_payout(self.Player,self.Computer) == True:
                continue
            
            user_raise = int(input("Player, how much do you want to raise?"))
            
            #add ante to the current bet
            self.Player.add_bet(user_raise)
            self.Computer.add_bet(user_raise)
            
            user_choice = int(input("Player, hit (1) or stay (0)?"))
            
            while user_choice ==1:
            
                self.Player.draw_card(self.game_deck.deal_card())
                print("Player: ")
                self.Player.player_show_hand()
            
                user_choice = int(input("Player, hit (1) or stay (0)?"))
            
            #cpu keeps drawing cards until hand score > 16
            cpu_hand_score = self.calc_hand_score(self.Computer.get_hand())
            
            while cpu_hand_score < 16:
                
                #draw card
                self.Computer.draw_card(self.game_deck.deal_card())
                print("CPU: ")
                self.Computer.player_show_hand()
                
                #update hand score
                cpu_hand_score = self.calc_hand_score(self.Computer.get_hand())
            
            #calculate total value of hand 
            player_hand_score = self.calc_hand_score(self.Player.get_hand())
            self.Player.set_hand_score(player_hand_score)
            self.Computer.set_hand_score(cpu_hand_score)
            
            #identify the winner of the round
            self.calc_winner_round()
            
            user_play = int(input("Do you want to continue? 1 = Continue, 0 = Quit"))
    
    def blackjack_payout(self,player,computer):
        """Calculates payout for player if the first 2 cards is 21."""
        if self.determine_black_jack(player) == True:
            
            if self.determine_black_jack(computer) == False:
                
                #add the bet to the game
                computer.add_bet(computer.get_current_bet()*1.5)
                
                #add computers bet to player
                player.add_to_purse(computer.get_current_bet())
                
                player.reset_bet()
                computer.reset_bet()
                
                player.reset_hand()
                computer.reset_hand()
                
            return True
            
        else:
            if self.determine_black_jack(computer) == True:
                
                #add the bet to the game
                player.add_bet(computer.get_current_bet()*1.5)
                
                #add players bet to computer
                computer.add_to_purse(player.get_current_bet())
                
                player.reset_bet()
                computer.reset_bet()
                
                player.reset_hand()
                computer.reset_hand()            
            
                return True
    def determine_black_jack(self,player):
        """determines if player or computer gets 21 with first 2 cards."""
        return self.calc_hand_score(player.get_hand()) == 21
        
    def deal_hand_initial(self,Player):
        """Deal the first 2 cards to the player."""
        Player.set_hand(self.game_deck.deal_card())
        Player.set_hand(self.game_deck.deal_card())
    
    def calc_winner_round(self):
        """
        Determine the winner for each round.
        """
        player_score = self.Player.get_hand_score()
        cpu_score = self.Computer.get_hand_score()
        
        print("Player Hand: ", player_score)
        print("CPU hand: ", cpu_score)
        
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

def test3():
    """Test playgame function."""
    bj = blackjack_game(20)
    
    bj.play_game(5)
    
if __name__ == "__main__":
    test()
    print("----")
    test2()
    print("test_3")
    test3()
