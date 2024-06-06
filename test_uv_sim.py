import unittest
from unittest.mock import patch
import uv_sim

class TestUVSimInstructions(unittest.TestCase):
    def setUp(self):
        """Initialize the simulator with empty memory and default state."""
        self.sim = uv_sim.UVSim()
        self.sim.memory = [0] * 100  # Assuming 100 memory slots for simplicity

    def load_and_run(self, instructions, inputs=None):
        """Load instructions into the simulator and run, with optional inputs."""
        if inputs is not None:
            with patch('builtins.input', side_effect=inputs):
                self.sim.load_program(instructions)
                self.sim.run()
        else:
            self.sim.load_program(instructions)
            self.sim.run()
        return self.sim.display_memory()

    def test_read_instruction(self):
        """Test reading an input into a specific memory location."""
        instructions = [1005, 4300]  # Read into location 5, halt
        expected_memory = self.load_and_run(instructions, inputs=["25"])
        self.assertEqual(eval(expected_memory)[5], 25)

    def test_write_instruction(self):
        """Test writing a memory location's value to output."""
        instructions = [1005, 1105, 4300]  # Read into 5, write 5, halt
        expected_output = "25"
        with patch('builtins.print') as mocked_print:
            self.load_and_run(instructions, inputs=["25"])
            mocked_print.assert_called_with(f"Value at memory location 5: 25")

    def test_load_store_instruction(self):
        """Test loading and storing values."""
        instructions = [1005, 2005, 2106, 4300]  # Read into 5, load 5 to acc, store acc to 6, halt
        expected_memory = self.load_and_run(instructions, inputs=["30"])
        self.assertEqual(eval(expected_memory)[6], 30)

    def test_add_subtract_instruction(self):
        """Test addition and subtraction."""
        instructions = [1005, 1006, 2005, 3006, 2107, 2005, 3106, 2108, 4300]  # Setup, add, subtract, halt
        expected_memory = self.load_and_run(instructions, inputs=["20", "10"])
        memory = eval(expected_memory)
        self.assertEqual(memory[7], 30)  # 20 + 10
        self.assertEqual(memory[8], 10)  # 20 - 10

    def test_multiply_divide_instruction(self):
        """Test multiplication and division."""
        instructions = [1005, 1006, 2005, 3306, 2107, 2005, 3206, 2108, 4300]  # Setup, multiply, divide, halt
        expected_memory = self.load_and_run(instructions, inputs=["12", "3"])
        memory = eval(expected_memory)
        self.assertEqual(memory[7], 36)  # 12 * 3
        self.assertEqual(memory[8], 4)  # 12 / 3

    def test_branch_instructions(self):
        """Test unconditional and conditional branches."""
        instructions = [1005, 4107, 2005, 3105, 4209, 1105, 4300, 4300, 1106, 4300]  # Complex branch logic
        expected_memory = self.load_and_run(instructions, inputs=["0"])
        memory = eval(expected_memory)
        self.assertEqual(memory[5], 0)
        # Further assertions depending on branch outcomes

if __name__ == '__main__':
    unittest.main()
