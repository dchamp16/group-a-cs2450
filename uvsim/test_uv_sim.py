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
        expected_memory = self.load_and_run(instructions, inputs=["0025"])
        self.assertEqual(eval(expected_memory)[5], 25)

    def test_write_instruction(self):
        """Test writing a memory location's value to output."""
        instructions = [1005, 1105, 4300]  # Read into 5, write 5, halt
        with patch('builtins.print') as mocked_print:
            self.load_and_run(instructions, inputs=["0025"])
            calls = mocked_print.call_args_list
            printed_lines = [call.args[0] for call in calls]
            expected_output = "Value at memory location 5: 25"
            assert expected_output in printed_lines, f"{expected_output} not found in printed output"

    def test_load_store_instruction(self):
        """Test loading and storing values."""
        instructions = [1005, 2005, 2106, 4300]  # Read into 5, load 5 to acc, store acc to 6, halt
        expected_memory = self.load_and_run(instructions, inputs=["0030"])
        self.assertEqual(eval(expected_memory)[6], 30)

    def test_add_subtract_instruction(self):
        """Test addition and subtraction."""
        instructions = [1009, 1010, 2009, 3010, 2111, 2009, 3110, 2112, 4300]  # Setup, add, subtract, halt
        expected_memory = self.load_and_run(instructions, inputs=["0020", "0010"])
        memory = eval(expected_memory)
        self.assertEqual(memory[11], 30)  # 20 + 10
        self.assertEqual(memory[12], 10)  # 20 - 10
        
    def test_add_subtract_instruction_2(self):
        """Test addition and subtraction with second argument."""
        instructions = [1009, 1010, 2009, 3010, 2111, 2009, 3110, 2112, 4300]  # Setup, add, subtract, halt
        expected_memory = self.load_and_run(instructions, inputs=["5000", "4999"])
        memory = eval(expected_memory)
        self.assertEqual(memory[11], 9999)  # 20 + 10
        self.assertEqual(memory[12], 1)  # 20 - 10


    def test_multiply_divide_instruction(self):
        """Test multiplication and division."""
        instructions = [1009, 1010, 2009, 3310, 2111, 2009, 3210, 2112, 4300]  # Setup, multiply, divide, halt
        expected_memory = self.load_and_run(instructions, inputs=["0012", "0003"])
        memory = eval(expected_memory)
        self.assertEqual(memory[11], 36)  # 12 * 3
        self.assertEqual(memory[12], 4)  # 12 / 3
    def test_multiply_divide_instruction_2(self):
        """Test multiplication and division with second argument."""
        instructions = [1009, 1010, 2009, 3310, 2111, 2009, 3210, 2112, 4300]  # Setup, multiply, divide, halt
        expected_memory = self.load_and_run(instructions, inputs=["0033", "0023"])
        memory = eval(expected_memory)
        self.assertEqual(memory[11], 759)  # 12 * 3
        self.assertEqual(memory[12], 1)  # 12 / 3

    def test_branch_instructions(self):
        """Test unconditional and conditional branches."""
        instructions = [1005, 4107, 2005, 3105, 4209, 1105, 4300, 4300, 1106, 4300]  # Complex branch logic
        expected_memory = self.load_and_run(instructions, inputs=["0000"])
        memory = eval(expected_memory)
        self.assertEqual(memory[5], 0)

    def test_loop_implementation(self):
        """Test loop implementation to display how conditionals branches execute.
        This code will take an input from -9999-9999 and count up or down until it gets to 0."""
        instructions = [1, 1012, 2012, 2113, 4210, 4108, 3100, 4003, 3000, 4003, 2113, 4300, 0000, 0000]
        expected_memory = self.load_and_run(instructions, inputs=["0100"])
        memory = eval(expected_memory)
        self.assertEqual(memory[12], 100)
        self.assertEqual(memory[13], 0)
        
    def test_usecase_create_bridge_to_assembly(self):
        """Test Use Case 3: Create a bridge to learning Assembly language"""
        instructions = [1007, 2007, 2108, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0020"])
        memory = eval(expected_memory)
        self.assertEqual(memory[8], 20)
        
    def test_usecase_analyze_conditionals(self):
        """Test Use Case 6: Analyze low level conditionals"""
        instructions = [1007, 2007, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0010"])
        memory = eval(expected_memory)
        self.assertEqual(memory[7], 10)
        
    def test_usecase_learn_early_computing(self):
        """Test Use Case 7: Learn the basics of early computing"""
        instructions = [1007, 2007, 2111, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0025"])
        memory = eval(expected_memory)
        self.assertEqual(memory[11], 25)
        
    def test_usecase_introduction_to_memory_manipulations(self):
        """Test Use Case 10: Introduction to memory manipulations"""
        instructions = [1007, 2007, 2108, 1108, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0030"])
        memory = eval(expected_memory)
        self.assertEqual(memory[8], 30)

    def test_conditional_branch_on_zero(self):
        """Test branching if accumulator is zero."""
        instructions = [1005, 2005, 3105, 4210, 1105, 4300, 1106, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0000"])
        self.assertEqual(eval(expected_memory)[5], 0)

    def test_conditional_branch_on_negative(self):
        """Test branching if accumulator is negative."""
        instructions = [1005, 2005, 3106, 4210, 1105, 4300, 1106, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0020", "0030"])
        self.assertEqual(eval(expected_memory)[5], 20)

    def test_memory_initialization(self):
        """Test if memory is initialized correctly."""
        self.assertEqual(self.sim.memory, [0] * 100)

    def test_full_program_execution(self):
        """Test a complete program execution."""
        instructions = [
            1007,
            2007,
            2108,
            1108,
            4300
        ]
        expected_memory = self.load_and_run(instructions, inputs=["0050"])
        memory = eval(expected_memory)
        self.assertEqual(memory[8], 50)

    def test_conditional_branch_on_positive(self):
        """Test branching if accumulator is positive."""
        instructions = [1005, 2005, 3000, 4210, 1105, 4300, 1106, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["0020"])
        self.assertEqual(eval(expected_memory)[5], 20)

    def test_program_with_comments(self):
        """Test a program that includes comments (ignoring comments)."""
        instructions = [
            1007,
            2007,
            2108,
            4300
        ]
        expected_memory = self.load_and_run(instructions, inputs=["0015"])
        memory = eval(expected_memory)
        self.assertEqual(memory[8], 15)

    def test_large_number_arithmetic(self):
        """Test handling of arithmetic operations with large numbers."""
        instructions = [1009, 1010, 2009, 3010, 2111, 2009, 3110, 2112, 4300]
        expected_memory = self.load_and_run(instructions, inputs=["9999", "0001"])
        memory = eval(expected_memory)
        self.assertEqual(memory[11], 10000)
        self.assertEqual(memory[12], 9998)

if __name__ == '__main__':
    unittest.main()
