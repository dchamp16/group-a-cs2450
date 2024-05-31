class UVSim:
    def __init__(self):
        # initialize memory, accumulator and instruction pointers
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_pointer = 0

    def load_program_from_file(self, file_path):
        """"
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
        # Executes the machine language program loaded into the UVSim memory
        pass

    def handle_instruction(self, opcode, operand):
        # handles the execution of the single instruction based on the opcode and operand
        pass
