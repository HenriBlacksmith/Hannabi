'''
    @author: HenriBlacksmith
'''

class Card(object):
    # -- builder
    def __init__(self, color, number, id):
        self.__color = color
        self.__number = number
        self.__id = id
    
    # -- getters
    def get_color(self):
        return self.__color
    
    def get_number(self):
        return self.__number
    
    def get_id(self):
        return self.__id
    
    # -- public methods
    def display_card(self):
        print self.get_color(), self.get_number()
        