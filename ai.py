from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = 'Robot Spock'

    def choose_gesture(self):
        print('AIs gesture is...')
        selected_gesture = random.choice(self.gesture_lists)
        self.gesture_selected = selected_gesture
        print(f'{self.gesture_selected}')
