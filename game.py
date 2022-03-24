from humans import Humans
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Humans()
        self.player2 = None
    
    def run_game(self):
        pass

    def display_greeting(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        print('------------------------------------------')
        print('Before we begin, lets take a look at the rules of the game.')
        print('------------------------------------------')
        print('-Scissors cut Paper')
        print('-Paper covers Rock')
        print('-Rock crushes Lizard')
        print('-Lizard poisons Spock')
        print('-Spock smashes Scissors')
        print('-Scissors decapitates Lizard')
        print('-Lizard eats Paper')
        print('-Paper disproves Spock')
        print('-Spock vaporizes Rock')
        print('-Rock crushes Scissors')

    def game_type(self):
        pick_game = int(input("Please choose '1' for Single Player or '2' for Multi-player: "))
        game_type = False
        

        while game_type is False:
            if pick_game == 1 or pick_game == 2:
                if pick_game == 1:
                    self.player2 = AI()
                    self.player1.set_name()
                    self.player2.set_name()
                    print("Single Player Chosen")
                    game_type = True
                elif pick_game == 2:
                    self.player2 = Humans()
                    self.player1.set_name()
                    self.player2.set_name()
                    print("Multi-Player Chosen")
                    game_type = True









