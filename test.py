import unittest
import subprocess

class TestMaze(unittest.TestCase):
    def test_invalid_maze(self):
        # test if invalid maze will throw out execptions
        result = subprocess.run(
            ["./maze", "test_data/invalid_4x4.txt"],
            capture_output=True, text=True
        )
        self.assertIn("Error", result.stderr)  # check wrong output

    def test_wall_collision(self):
        # test over area situation
        result = subprocess.run(
            ["./maze", "test_data/valid_5x5.txt"],
            input="W\n", text=True, capture_output=True
        )
        self.assertIn("Cannot move", result.stdout)

if __name__ == "__main__":
    unittest.main()