import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import Account
import Card

Root = "api.bearRobotics.com/ATM"  # API Root url

# Alert
def Alert(text):
    print("====================================")
    print("===============Alert================")
    print("====================================")
    print("=>", text)

# check card valid => return Verification PIN_Number
def CheckCard(cardNumber, PIN):
    datas = { 'cardNumber' : cardNumber, 'PIN' : PIN }
    url = Root + "/CheckCard"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response.status_code

def EjectCard():
    # card eject
    return True

def EjectMoney():
    # card eject
    return True

def GetAccount(cardNumber, PIN):
    # get balance
    datas = { 'cardNumber' : cardNumber, 'PIN' : PIN }
    url = Root + "/GetBalnaceAccount"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response

def Balance(_Account):
    Alert("your balance is ", _Account.Balance)
    return _Account.Balance
  
def Deposit(_Account, IN):

    Balance = _Account.Balance + IN
    
    # save balance
    datas = { 'Balance' : Balance }
    url = Root + "/Deposit"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response

def Withdrawal(Balance, Out):
    Balance = Balance + Out
    
    # save balance
    datas = { 'Balance' : Balance }
    url = Root + "/Withdrawal"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    
    response = requests.post(url, data=datas, headers=headers)
    return response

def main(_Account, _Card):

    while True:

        Alert("Please Enter your Card. If you want to exit the program, Press 0")
        CardNumber, PIN = input() # contains PIN Number

        # if user press 0 => exit
        if CardNumber == 0:
            exit()

        _Card.set([CardNumber, PIN]) # set

        result = await CheckCard(_Card.Number, _Card.PIN) # check card validation


        if result == "Sucess":
            Alert("Press 1 to balance check or 2 to deposit money or 3 to withdrawal money")
            order = input()  # Balance // Deposit // Withdrawal

            # class
            balance_information = await GetAccount(_Card.Number, _Card.PIN)
            _Account.set(balance_information)

            if order == 1:
                Balance(_Account)

            if order == 2:
                Alert("Choose the amount to deposit")
                IN = input()

                Alert("Please Enter money")
                Money = input()

                if IN != Money:
                    Alert("The deposit amount is different. Please try again")
                    EjectMoney() # Money Eject
                    EjectCard() # Card Eject

                if IN == Money:
                    Deposit_result = Deposit(_Account, IN, Money)

                    if Deposit_result.status_code == "Fail":
                        Alert("Error : The deposit operation did not proceed. Please try again")

                    if Deposit_result.status_code == "Sucess":
                        Alert(IN + "$ has been deposited into your account. The remaining balance is" + Deposit_result.Balance)

            if order == 3:
                Alert("Choose the amount to withdrawal")
                Out = input()

                if Out > _Account.Balance:
                    Alert("The withdrawal amount is greater than your balance. Please try again")
                    EjectMoney() # Money Eject
                    EjectCard() # Card Eject

                else:
                    Withdrawal_result = Withdrawal(_Account, Out)

                    if Withdrawal_result.status_code == "Fail":
                        Alert("Error : The withdrawal operation did not proceed. Please try again")

                    if Withdrawal_result.status_code == "Sucess":
                        Alert(Out + "$ has been withdrawn from your account. The remaining balance is" + Withdrawal_result.Balance)

        else:
            Alert("Error : Card is invalid") # Alert

if __name__ == "__main__":


    _Account = Account() # account information
    _Card = Card() # Card information

    main(_Account, _Card)

    os.execl(sys.executable, sys.executable, *sys.argv) # loop