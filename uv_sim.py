from instructions import read_instruction, write_instruction, load_instruction, \
    store_instruction, add_instruction, subtract_instruction, divide_instruction, multiply_instruction, \
    branch_instruction, branchneg_instruction, branchzero_instruction, halt_instruction


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
        execute the appropriate instruction based on the opcode and operand

        :param opcode (int): dictates which operation to perform
        :param operand (int): memory address
        :return (bool): true if instruction was successful, false if error occurred
        """
        instruction_set = {
            10: read_instruction,
            11: write_instruction,
            20: load_instruction,
            21: store_instruction,
            30: add_instruction,
            31: subtract_instruction,
            32: divide_instruction,
            33: multiply_instruction,
            40: branch_instruction,
            41: branchneg_instruction,
            42: branchzero_instruction,
            43: halt_instruction
        }

        if operand < 0 or operand >= len(self.memory):
            print(f"Error: Operand {operand} out of memory range.")
            return False

        func = instruction_set.get(opcode)
        if func:
            try:
                return func(self, operand)
            except Exception as e:
                print(f"Error executing {opcode} with operand {operand}: {e}")
                return False
        else:
            print(f"Invalid opcode: {opcode}")
            return False

# This is a potential script given the class for the UVSim etc.
# from instructions import Instructions, (
#     read_instruction, write_instruction, load_instruction,
#     store_instruction, add_instruction, subtract_instruction,
#     divide_instruction, multiply_instruction, branch_instruction,
#     branch_neg_instruction, branch_zero_instruction, halt_instruction
# )
# from utils import parse_instruction, read_program

# class UVSim:
#     def __init__(self):
#         self.memory = [0] * 100
#         self.accumulator = 0
#         self.instruction_counter = 0
#         self.halted = False

#     def load_program(self, program):
#         for i, instruction in enumerate(program):
#             self.memory[i] = instruction

#     def fetch(self):
#         return self.memory[self.instruction_counter]

#     def execute(self):
#         while not self.halted:
#             instruction = self.fetch()
#             op_code, operand = parse_instruction(instruction)
#             self.instruction_counter += 1
#             self.decode_and_execute(op_code, operand)

#     def decode_and_execute(self, op_code, operand):
#         if op_code == Instructions.READ:
#             read_instruction(self, operand)
#         elif op_code == Instructions.WRITE:
#             write_instruction(self, operand)
#         elif op_code == Instructions.LOAD:
#             load_instruction(self, operand)
#         elif op_code == Instructions.STORE:
#             store_instruction(self, operand)
#         elif op_code == Instructions.ADD:
#             add_instruction(self, operand)
#         elif op_code == Instructions.SUBTRACT:
#             subtract_instruction(self, operand)
#         elif op_code == Instructions.DIVIDE:
#             divide_instruction(self, operand)
#         elif op_code == Instructions.MULTIPLY:
#             multiply_instruction(self, operand)
#         elif op_code == Instructions.BRANCH:
#             branch_instruction(self, operand)
#         elif op_code == Instructions.BRANCHNEG:
#             branch_neg_instruction(self, operand)
#         elif op_code == Instructions.BRANCHZERO:
#             branch_zero_instruction(self, operand)
#         elif op_code == Instructions.HALT:
#             halt_instruction(self, operand)
