import keyboard
import time
from src.mouse_controller import MouseController
from src.keyboard_controller import KeyboardController

class AFKController:
    def __init__(self):
        self.mouse_controller = MouseController()
        self.keyboard_controller = KeyboardController()

    def start_afk(self):
        """Start the AFK routine."""
        print("AFK mode activated. Press F7 to stop.")
        while True:
            if keyboard.is_pressed('f7'):
                print("Stopping AFK mode...")
                break
            self.mouse_controller.move_in_circle()
            self.keyboard_controller.press_space()

    def run(self):
        """Main entry for the AFK controller."""
        print("Press F7 to start AFK mode.")
        while True:
            if keyboard.is_pressed('f7'):
                self.start_afk()
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            time.sleep(0.1)
