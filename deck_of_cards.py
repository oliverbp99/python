class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __add__(self, other):
        return self.cards + self.other

    def __getitem__(self, key):
        return self.cards[key]
    
    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f'(self.__dict__)'

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del(self.cards[key])

    def __str__(self):
        return f'Cards: (self.cards)'


    