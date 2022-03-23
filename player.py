# Parent Class to support Human/AI class

class Player:
    def __init__(self):
        self.gesture_lists = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.wins = 0
        self.name = ''
        self.gesture_selected = ''

    def choose_gesture(self):
        pass 
    #Method Will Method Overide in Child Class