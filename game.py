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
        print('Best out of three wins')

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

    def game_play(self):
        round_count = 1
    
        while self.player1.wins < 2 and self.player2.wins < 2:
            print(f'Lets start Round {round_count}')
            self.player1.choose_gesture()
            self.player2.choose_gesture()

            if self.player1.gesture_selected == self.player2.gesture_selected:
                print('Tie')
                round_count += 1
            elif self.player1.gesture_selected == self.player1.gesture_lists[0] and self.player2.gesture_selected == self.player2.gesture_lists[2]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[0]} beats {self.player2.gesture_lists[2]}.')
            elif self.player1.gesture_selected == self.player1.gesture_lists[0] and self.player2.gesture_selected == self.player2.gesture_lists[3]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[0]} beats {self.player2.gesture_lists[3]}.')    
            elif self.player1.gesture_selected == self.player1.gesture_lists[2] and self.player2.gesture_selected == self.player2.gesture_lists[1]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[2]} beats {self.player2.gesture_lists[1]}.') 
            elif self.player1.gesture_selected == self.player1.gesture_lists[2] and self.player2.gesture_selected == self.player2.gesture_lists[3]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[2]} beats {self.player2.gesture_lists[3]}.')
            elif self.player1.gesture_selected == self.player1.gesture_lists[1] and self.player2.gesture_selected == self.player2.gesture_lists[0]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[1]} beats {self.player2.gesture_lists[0]}.')
            elif self.player1.gesture_selected == self.player1.gesture_lists[1] and self.player2.gesture_selected == self.player2.gesture_lists[4]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[1]} beats {self.player2.gesture_lists[4]}.')
            elif self.player1.gesture_selected == self.player1.gesture_lists[3] and self.player2.gesture_selected == self.player2.gesture_lists[4]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[3]} beats {self.player2.gesture_lists[4]}.')
            elif self.player1.gesture_selected == self.player1.gesture_lists[3] and self.player2.gesture_selected == self.player2.gesture_lists[1]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[3]} beats {self.player2.gesture_lists[1]}.')    
            elif self.player1.gesture_selected == self.player1.gesture_lists[4] and self.player2.gesture_selected == self.player2.gesture_lists[2]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[4]} beats {self.player2.gesture_lists[2]}.')
            elif self.player1.gesture_selected == self.player1.gesture_lists[4] and self.player2.gesture_selected == self.player2.gesture_lists[0]:
                self.player1.wins += 1
                round_count += 1
                print(f'{self.player1.name} wins the round. {self.player1.gesture_lists[4]} beats {self.player2.gesture_lists[0]}.')








