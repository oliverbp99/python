class P:
    def __init__(self, name, amount):
        self.amount = amount

    @property # getter
    def amount(self):
        return self.__amount
    
    @amount.setter # setter
    def amount(self, amount):

        self.__amount = amount

        """
        if amount < 0:
            self.__amount = 0
        elif amount > 1000:
            self.__amount = 1000
        else:
            self.__amount = amount
        """