# User account information
class Account:
    def __init__(self):
        self.Id = ""
        self.Balance = 0
        
    def set(self, value):
        self.Id = value[0]
        self.Balance = value[1]
        return self.Balance
