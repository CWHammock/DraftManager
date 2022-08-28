from cmath import log
import logging
import time

logging.basicConfig(format='%(asctime)s %(message)s', filename='draftmanager.log', filemode='a', level=logging.INFO)

class Player:
    def __init__(self, name, amount):
        self.name = name
        self.money = int(amount)
        logging.info(f"Player created with name {self.name} and amount of {self.money} ")
    
    def modify_amount(self, amount):
        self.money = amount
        print(f'Player {self.name} having his amount changed to {self.money}')
        logging.info(f'Player {self.name} having his amount changed to {self.money}')
        
    def __repr__(self):
        return f'Name {self.name} Amount {self.money}'
    
    def lower_amount(self, number):
        self.money = int(self.money - number)
        print(f'Amount {number} was taken from {self.name} bringing them to {self.money}')
        logging.info(f'Amount {number} was taken from {self.name} bringing them to {self.money}')
    
    def get_name(self):
        return str(self.name)
    
    def get_amount(self):
        return int(self.money)
    
   

def menu(players,number_of_players):
    
    ans=True
    while ans: 
        print("++++++++++ Draftmanager ++++++++++++++")
        for i in range(number_of_players):
            logging.info(players[i])
            print(players[i])       
        print ('1 -- Deduct Amount' )
        print ('2 -- Modify Amount (if mistake for deducting)' )
        print ('4 -- Exit' )
        option = input('Enter your choice: ')
        if option == '1':
            while True:
                name = input(f"Enter name of player to deduct: ")
                deduct = int(input(f"Enter name the amount to deduct: "))
                name_f = input(f"Is {name} and {deduct} correct? or break with \'b\' ")
                if name_f == 'b' or name_f == 'break':
                    break
                if  name_f == 'y' or name_f == 'yes' or name_f == 'Y' or name_f == 'Yes':
                    counter = 0
                    for x in players:
                        if x.get_name() == name:
                            x.lower_amount(deduct)
                            counter = 1
                    if counter == 0:
                        print(f"That {name} is not a player... try again")
                        continue        
                    break
                                
        elif option == '2':
            while True:
                name = input(f"Enter name of player to modify amount: ")
                deduct = int(input(f"Enter name the amount to change amount to: "))
                name_f = input(f"Is {name} amount getting changed to {deduct} correct? or break with \'b\'")
                if name_f == 'b' or name_f == 'break':
                    break
                if  name_f == 'y' or name_f == 'yes' or name_f == 'Y' or name_f == 'Yes':
                    counter = 0
                    for x in players:
                        if x.get_name() == name:
                            x.modify_amount(deduct)
                            counter = 1
                    if counter == 0:
                        print(f"That {name} is not a player... try again")
                        continue        
                    break
        elif option == '3':
            print('Great Draft....Warren is the man')
            ans = False
            break
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
    
def main():
    players = []
    starting_value = 0
    number_of_players = 0
    money_answer = False
    while True:
        starting_value = int(input("What is the starting amount for each player: ? "))
        number_of_players = int(input("What is the number of players: ? "))
        answer = input(f"is the number of players {number_of_players} and the starting amount {starting_value}? ")
        if answer == 'y' or answer == 'yes' or answer == 'Y' or answer == 'Yes':
            logging.info(f"Game setup: number of players: {number_of_players}: starting amount: {starting_value}")
            break
    print(f"Setting Game up....")
    time.sleep(0)
    for i in range(number_of_players):
        name_correct = False
        while True:
            name = input(f"Enter name of player {i}: ")
            name_f = input(f"Is {name} correct? ")
            if  name_f == 'y' or name_f == 'yes' or name_f == 'Y' or name_f == 'Yes':
                players.append(Player(name,starting_value))
                break
    menu(players, number_of_players)
    
    

main()