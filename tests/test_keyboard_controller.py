import unittest
from src.keyboard_controller import KeyboardController

class TestKeyboardController(unittest.TestCase):
    def test_press_space(self):
        keyboard_controller = KeyboardController()
        # We'll just verify the object initialization for now
        self.assertIsInstance(keyboard_controller, KeyboardController)

if __name__ == '__main__':
    unittest.main()
