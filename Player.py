class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def pop_one(self):
        if len(self.all_cards) != 0:
            return self.all_cards.pop()
        
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return 'Player {} has {} cards left'.format(self.name,len(self.all_cards))
