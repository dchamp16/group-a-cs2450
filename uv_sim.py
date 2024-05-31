from instructions import mock_instruction, halt_instruction


class UVSim:
    def __init__(self):
        # initialize memory, accumulator and instruction pointers
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_pointer = 0

    def load_program_from_file(self, file_path):
        """
        loads a Basicml program from a file into UVSIM memory
        each line of the file is contain one instruction written as a 4 digit decimal number

        parameter:
        file_path (str): the path to the file to load BasicML program
        """
        try:
            with open(file_path, 'r') as file:
                line_count = 0
                for i, line in enumerate(file):
                    if line.strip():  # Ensure the line is not empty.
                        self.memory[i] = int(line.strip())  # Convert line to integer and store in memory.
                        line_count += 1
            print(f"Successfully loaded {line_count} instructions into memory.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except ValueError:
            print("Error: All lines in the input file must contain valid integer values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def execute_program(self):
        try:
            while True:
                if self.instruction_pointer >= len(self.memory):
                    print("End of memory without encountering HALT")
                    break

                instruction = self.memory[self.instruction_pointer]
                opcode = instruction // 100
                operand = instruction % 100
                self.instruction_pointer += 1 # this will move to the next instruction

                if not self.handle_instruction(opcode, operand):
                    print(f"Execute halted unexpectedly at instruction {instruction}")
                    break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_instruction(self, opcode, operand):
        # handles the execution of the single instruction based on the opcode and operand
        """
        Mock handler for instruction to test the execution flow

        :param opcode:
        :param operand:
        :return:
        """
        instruction_set = {
            10: mock_instruction,  # Read
            11: mock_instruction,  # Write
            20: mock_instruction,  # Load
            21: mock_instruction,  # Store
            30: mock_instruction,  # Add
            31: mock_instruction,  # Subtract
            32: mock_instruction,  # Divide
            33: mock_instruction,  # Multiply
            40: mock_instruction,  # Branch
            41: mock_instruction,  # Branch if negative
            42: mock_instruction,  # Branch if zero
            43: halt_instruction  # Halt
        }
        func = instruction_set.get(opcode)
        if func:
            return func(self, operand)
        else:
            print(f"Invalid opcode: {opcode}")
            return False

