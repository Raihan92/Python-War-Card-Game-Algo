class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def cards_shuffle(self):
        random.shuffle(self.all_cards)
        
    def pop_one(self):
        return self.all_cards.pop()
