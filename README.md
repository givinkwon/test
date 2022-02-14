Write code for a simple ATM. It doesn't need any UI (either graphical or console), but a controller should be implemented and tested.



Requirements
At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw



For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.



Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.



A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.



Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.



You can simplify some complex real world problems if you think it's not worth illustrating in the project.



How to submit
Please upload the code for this project to GitHub or anywhere, and post a link to your repository below. Please attach the instruction to clone your project, build and run tests in README.md file in the root directory of the repository.










< Code Description > 
1. To start an ATM controller, run main.py.
2. The main function defines the following functions. Some functions are abstracted.
- Alert: Guide the user to a message.
- CheckCard : Validate the card based on CardNumber and PIN information.
- ObjectCard: Method of sending out a card in case of an error.
- Object Money: Method of sending money deposited in case of an error
- GetAccount : Get the account information based on CardNumber and PIN information.
- Balance: Here's a message to check your balance.
- Deposit: Process the deposit as much as the amount entered and guide the message.
- Withdrawal: Process withdrawal by the amount entered and guide the message.

3. Card and Account Class were defined for use in the main function. These are Card.py and Account, respectively.It's defined in py.

4. We conducted a simple test using the unittest library. Some tests are abstracted.
