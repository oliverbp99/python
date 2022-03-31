class Bank:
    def __init__(self):
        self.accounts = []


class Account:
    def __init__(self, number, cust):
        self.number = number
        self.cust = cust



class Customer:
    def __init__(self, name):
        self.name = name
