from humans import Humans
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Humans()
        self.player = None
    
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

        


