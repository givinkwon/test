
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

def Balance():
    
  
def Deposit():
    
def Withdrawal():


def main(_CardNumber, order):
    result = await checkCard(_CardNumber)
    
    if result == "OK":
        PIN = input()
        check_PIN = await InsertPIN(PIN)
        
        if check_PIN == "OK":
            if order == "Balance":
                
            if order == "Deposit":
                
            if order == "Withdrawal":
                
        else:
            Alert("Error : PIN is invalid") # Alert
    else:
        Alert("Error : Card is invalid") # Alert

if __name__ == "__main__":
    cardNumber = input() # contains PIN Number
    order = input() # Balance // Deposit // Withdrawal
    main(cardNumber, order)
