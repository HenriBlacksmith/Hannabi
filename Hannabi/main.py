'''
    Hanabi\main.py
    @author: HenriBlacksmith
'''
# -- imports
from Game import Game
'''
Tasks :
- Mix the card pile
- Provide every player with five cards
- 
'''
game = Game()
game.generate_card_shoe()
game.add_player('Henry')
game.add_player('Joe')
game.distribute_card_hands()
game.show_hands()