import pyautogui
import math
import time

class MouseController:
    def __init__(self, radius=100, speed=0.05):
        self.center_x, self.center_y = pyautogui.size()[0] // 2, pyautogui.size()[1] // 2
        self.radius = radius
        self.speed = speed

    def move_in_circle(self):
        """Move the mouse in a circular path."""
        for angle in range(0, 360, 10):
            x = self.center_x + self.radius * math.cos(math.radians(angle))
            y = self.center_y + self.radius * math.sin(math.radians(angle))
            pyautogui.moveTo(x, y)
            time.sleep(self.speed)
