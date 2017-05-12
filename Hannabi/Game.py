'''
    @author: HenriBlacksmith
'''

class Game(object):
    def __init__(self):
        self.n_tokens = 8
        self.active_tokens = self.n_tokens
    
    # -- getters
    def get_tokens(self):
        return self.__Tokens
    
    # -- public methods
    def burn_token(self):
        self.active_tokens -= 1
        if self.active_tokens < 0:
            print 'Game Over'
        return None