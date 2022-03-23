from player import Player


class Humans(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input('Please enter name, ')
        
    def choose_gesture(self):
        gesture_confirmed = False
        print(f"Enter in '0' for {self.gesture_list[0]}")
        print(f"Enter in '1' for {self.gesture_list[1]}")
        print(f"Enter in '2' for {self.gesture_list[2]}")
        print(f"Enter in '3' for {self.gesture_list[3]}")
        print(f"Enter in '4' for {self.gesture_list[4]}")

        while gesture_confirmed is False:
            selected_gesture = int(input('Enter in the number (gesture) you want to play.'))
            if selected_gesture >= 0 and selected_gesture <= 4:
                if selected_gesture == 0:
                    self.gesture_selected = self.gesture_lists[0]
                    print("Gesture confirmed!")
                    gesture_confirmed = True
                elif selected_gesture == 1:
                    self.gesture_selected = self.gesture_lists[1]
                    print("Gesture confirmed!")
                    gesture_confirmed = True  
                elif selected_gesture == 2:
                    self.gesture_selected = self.gesture_lists[2]
                    print("Gesture confirmed!")
                    gesture_confirmed = True     
                elif selected_gesture == 3:
                    self.gesture_selected = self.gesture_lists[3]
                    print("Gesture confirmed!")
                    gesture_confirmed = True
                elif selected_gesture == 4:
                    self.gesture_selected = self.gesture_lists[4]
                    print("Gesture confirmed!")
                    gesture_confirmed = True
            else:
                print("Invaild number, please try again.") 
                
                       



           

        