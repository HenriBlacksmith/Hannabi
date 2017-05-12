'''
    @author: HenriBlacksmith
'''
# -- imports
from Card import Card

# -- class
class Player(object):
    def __init__(self, name):
        self.player_name = name
        self.card_hand = []
    
    # -- getters
    def get_name(self):
        return self.player_name
        
    # -- public methods
    def take_card(self, card):
        self.card_hand.append(card)
    
    def display_hand(self):
        print self.get_name()
        for card in self.card_hand:
            print card.display_card()     