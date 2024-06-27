import unittest
import io
from cpu import CPU
from memory import Memory
from app import app, uv_sim

class UVSimTestCase(unittest.TestCase):

    def setUp(self):
        """Initialize the test client and reset the simulator state before each test."""
        self.app = app.test_client()
        self.memory = Memory(100)
        self.app.testing = True
        self.cpu = CPU(self.memory)
        uv_sim.reset()  # Reset the simulator state before each test

    def test_index_get(self):
        """Test that the index route returns a 200 status code and contains the expected text."""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'UVSim Program Loader', result.data)

    def test_upload_multiple_files(self):
        """Test uploading multiple files and ensure the correct success message is displayed."""
        sample_program_1 = "+1009\n+2009\n+3009\n+4300\n-99999\n"
        sample_program_2 = "+1009\n+2009\n+3009\n+4300\n-99999\n"

        data = {
            'file': [
                (io.BytesIO(sample_program_1.encode()), 'test_program_1.txt'),
                (io.BytesIO(sample_program_2.encode()), 'test_program_2.txt')
            ]
        }

        result = self.app.post('/', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 302)  # Expect a redirect after POST
        follow_up = self.app.get('/')
        self.assertIn(b'Files loaded successfully.', follow_up.data)

    def test_user_input(self):
        """Test that user input is correctly handled and the program halts as expected."""
        sample_program = "+1009\n+2009\n+3009\n+2109\n+4300\n-99999\n"
        uv_sim.load_program([int(line.replace('+', '')) for line in sample_program.split()])
        uv_sim.run()

        result = self.app.post('/', data={
            'user_input': '0050'
        })

        self.assertEqual(result.status_code, 302)  # Expect a redirect after POST
        follow_up = self.app.get('/')
        self.assertIn(b'Program halted.', follow_up.data)

    def test_invalid_user_input(self):
        """Test that invalid user input is handled correctly."""
        sample_program = "+1009\n+2009\n+3009\n+4300\n-99999\n"
        uv_sim.load_program([int(line.replace('+', '')) for line in sample_program.split()])
        uv_sim.run()

        result = self.app.post('/', data={
            'user_input': 'abc'
        })

        self.assertEqual(result.status_code, 302)  # Expect a redirect after POST
        follow_up = self.app.get('/')
        self.assertIn(b'Please enter a 4-digit integer.', follow_up.data)

    def test_addition(self):
        program = [2010, 3010, 2110, 4300]  # LOAD 10, ADD 10, STORE 10, HALT
        self.memory[10] = 50
        self.cpu.load_program(program)
        self.cpu.run()
        self.assertEqual(self.memory[10], 100)

    def test_subtraction(self):
        program = [2010, 3110, 2110, 4300]  # LOAD 10, SUB 10, STORE 10, HALT
        self.memory[10] = 5
        self.cpu.load_program(program)
        self.cpu.run()
        self.assertEqual(self.memory[10], 0)

    def test_multiplication(self):
        program = [2010, 3310, 2110, 4300]  # LOAD 10, MUL 10, STORE 10, HALT
        self.memory[10] = 2
        self.cpu.load_program(program)
        self.cpu.run()
        self.assertEqual(self.memory[10], 4)

    def test_division(self):
        # Program for successful division
        program = [2010, 3220, 2110, 4300]  # LOAD 10, DIV 20, STORE 10, HALT
        self.memory[10] = 4
        self.memory[20] = 2
        self.cpu.load_program(program)
        self.cpu.run()
        self.assertEqual(self.memory[10], 2)  # Check successful division

        # Test for division by zero
        program = [2010, 3220, 4300]  # LOAD 10, DIV 20, HALT
        self.memory[10] = 4
        self.memory[20] = 0
        self.cpu.load_program(program)
        with self.assertRaises(ZeroDivisionError):
            self.cpu.run()

if __name__ == '__main__':
    unittest.main()
