
import os
import requests

def checkCard(number, order):
    # check card valid
    data = { 'number' : number }
    url = "check url"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response
    

def InsertPIN(PIN):
    # check PIN
    data = { 'pin' : PIN }
    url = "check url"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response

def GetBalnaceAccount(Account):
    # get balance
    data = { 'Account' : Account }
    url = "check url"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response

def Balance(balance):
    return Alert("your balance is ", balance)
  
def Deposit(Balance, IN):
    Balance = Balance + IN
    
    # save balance
    data = { 'Balance' : Balance }
    url = "check url"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return Alert("your balance is ", balance)

def Withdrawal(Balance, Out):
    Balance = Balance + Out
    
    # save balance
    data = { 'Balance' : Balance }
    url = "check url"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return Alert("your balance is ", balance)


def main(_CardNumber, order):
    result = await checkCard(_CardNumber)
    
    if result == "OK":
        PIN = input()
        check_PIN = await InsertPIN(PIN)
        
        if check_PIN == "OK":
            Account = input()
            # class
            Information = await GetBalnaceAccount(Account)
            
            if order == "Balance":
                Balance(Information.Balance)
            if order == "Deposit":
                IN = input()
                Deposit(Information.Balance, IN)
            if order == "Withdrawal":
                Out = input()
                Withdrawal(Information.Balance, Out)
        else:
            Alert("Error : PIN is invalid") # Alert
    else:
        Alert("Error : Card is invalid") # Alert

if __name__ == "__main__":
    cardNumber = input() # contains PIN Number
    order = input() # Balance // Deposit // Withdrawal
    main(cardNumber, order)
