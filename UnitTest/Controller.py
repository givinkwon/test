from unittest import TestCase
from main import *
import Account
import Card

class Controller(TestCase):
    def test_Account(self):
        _Account = Account()
        self.assertEqual(_Account.Id, "")
        self.assertEqual(_Account.Balance, 0)

        _Account.set(["test", 1])
        self.assertEqual(_Account.Id, "test")
        self.assertEqual(_Account.Balance, 1)

    def test_Card(self):
        _Card = Card()
        self.assertEqual(_Card.Number, 0)
        self.assertEqual(_Card.PIN, 0)

        _Card.set([1234, 1])
        self.assertEqual(_Card.Number, 1234)
        self.assertEqual(_Card.PIN, 1)


    def test_Balance(self):
        _Account = Account()
        _Account.set(["test", 5])

        result = Balance(_Account, 5)
        self.assertEqual(result, 5)

    def test_Deposit(self):
        _Account = Account()
        _Account.set(["test", 5])

        result = Deposit(_Account, 5)
        self.assertEqual(result.Balance, 10)

    def test_Withdrawal(self):
        _Account = Account()
        _Account.set(["test", 5])

        result = Withdrawal(_Account, 5)
        self.assertEqual(result.Balance, 0)

    def test_GetAccount(self):
        # error 1
        self.assertRaises(Exception, GetAccount(1234 - 2323 - 2323 - 3, ))

        # error 2
        self.assertRaises(Exception, GetAccount(1234 - 2323 - 2323 - 3, 231))

        # sucess
        balance_information = GetAccount(1234-2323-2323-3232, 5321)
        self.assertEqual(balance_information.status_code, "Sucess")

    def test_CheckCard(self):
        # sucess
        result = CheckCard(1234-2323-2323-3232, 5321)
        self.assertEqual(result.status_code, "Sucess")

    def test_EjectCard(self):
        pass

    def test_EjectMoney(self):
        pass