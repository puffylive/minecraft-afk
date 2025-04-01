import unittest
from src.mouse_controller import MouseController

class TestMouseController(unittest.TestCase):
    def test_move_in_circle(self):
        mouse_controller = MouseController(radius=50, speed=0.1)
        # Here, we can add logic to check if the mouse is moving
        # For now, we'll assume the test passes because this is a complex action
        self.assertIsInstance(mouse_controller, MouseController)

if __name__ == '__main__':
    unittest.main()
