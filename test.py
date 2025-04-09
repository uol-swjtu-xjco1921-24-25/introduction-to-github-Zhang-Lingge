import unittest
import subprocess
import os
import tempfile
from typing import List

class TestMazeGame(unittest.TestCase):
    C_SOURCE_FILE = "maze.c"
    
    INPUT_FILES = [
        "test_data/input/input_complete.txt",
        "test_data/input/input_over_area.txt",
        "test_data/input/input_normal.txt",
    ]
    
    INVALID_MAZE_FILES = [
        "test_data/invalid/invalid_invalid_character",
        "test_data/invalid/invalid_no_exit",
        "test_data/invalid/invalid_no_start",
        "test_data/invalid/invalid_too_large_101x101",
        "test_data/invalid/invalid_too_small_4x4",
        "test_data/invalid/ireg_height_5x5",
        "test_data/invalid/ireg_width_5x5",
    ]
    
    VALID_MAZE_FILES = [
        "test_data/valid/reg_5x5",
        "test_data/valid/reg_10x6",
        "test_data/valid/reg_15x8",
    ]

    @classmethod
    # compile c file
    def CompileC(cls):
        if not os.path.exists(cls.C_SOURCE_FILE):
            raise FileNotFoundError(f"C file doesn't exist: {cls.C_SOURCE_FILE}")
        
        cls.executable = tempfile.mktemp(prefix="maze_")
        compile_cmd = ["gcc", cls.C_SOURCE_FILE, "-o", cls.executable]
        
        try:
            subprocess.run(compile_cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Compile failed: {e.stderr.decode()}")

    # clear temporary files
    @classmethod
    def clrTemFile(cls):
        if os.path.exists(cls.executable):
            os.remove(cls.executable)

    # run maze and return result
    def run_maze(self, maze_file: str, input_file: str = None) -> subprocess.CompletedProcess:
        try:
            input_commands = None
            if input_file:
                with open(input_file, "r") as f:
                    input_commands = f.read()
            
            return subprocess.run(
                [self.executable, maze_file],
                input=input_commands,
                text=True,
                capture_output=True,
                timeout=5
            )
        except subprocess.TimeoutExpired:
            self.fail("Test timed out")

    # test data imported
    def test_1_valid_maze_loading(self):
        for maze_file in self.VALID_MAZE_FILES:
            with self.subTest(maze_file=maze_file):
                result = self.run_maze(maze_file)
                self.assertEqual(result.returncode, 0, f"Loading valid maze failed: {maze_file}")

    def test_2_invalid_maze_handling(self):
        for maze_file in self.INVALID_MAZE_FILES:
            with self.subTest(maze_file=maze_file):
                result = self.run_maze(maze_file)
                self.assertNotEqual(result.returncode, 0, f"Handling invalid maze failed: {maze_file}")

    def test_3_player_movement(self):
        test_cases = [
            (self.VALID_MAZE_FILES[0], self.INPUT_FILES[0], "You win"),
            (self.VALID_MAZE_FILES[0], self.INPUT_FILES[1], "Cannot move"),
            (self.VALID_MAZE_FILES[0], self.INPUT_FILES[2], "Player moved"),
        ]
        
        for maze_file, input_file, expected in test_cases:
            with self.subTest(maze_file=maze_file, input_file=input_file):
                result = self.run_maze(maze_file, input_file)
                self.assertIn(expected, result.stdout)

if __name__ == "__main__":
    unittest.main()
