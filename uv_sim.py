class UVSim:
    def __init__(self):
        # initialize memory, accumulator and instruction pointers
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_pointer = 0

    def load_program_from_file(self, file_path):
        # Loads a machine language program from a file into the UVSim memory
        pass

    def execute_program(self):
        # Executes the machine language program loaded into the UVSim memory
        pass

    def handle_instruction(self, opcode, operand):
        # handles the execution of the single instruction based on the opcode and operand
        pass
