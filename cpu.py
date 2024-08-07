class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True
        self.waiting_for_input = False
        self.input_operand = None
        self.write_outputs = []
        self.inputs = {}  # Initialize inputs dictionary

    def reset_state(self):
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True
        self.waiting_for_input = False
        self.input_operand = None
        self.inputs.clear()

    def load_program(self, program):
        """Load a program into memory."""
        if len(program) > len(self.memory):
            raise ValueError("Program size exceeds memory capacity")
        self.memory[:len(program)] = program
        self.reset_state()  # Reset the CPU state
        print(f"Program loaded into memory: {self.memory}")

    def run(self):
        print("Starting CPU execution")
        while self.running:
            if not self.waiting_for_input:
                instruction = self.fetch()
                if instruction is not None:
                    opcode, operand = self.decode(instruction)
                    self.execute(opcode, operand)
                    self.overflow_check()
            else:
                print("Waiting for input...")
                break
        if self.waiting_for_input:
            print("Execution paused for input.")
        else:
            print("CPU execution completed")

    def rerun(self):
        print("Starting CPU re-execution without input requests")
        self.reset_state()
        while self.running:
            instruction = self.fetch()
            if instruction is not None:
                opcode, operand = self.decode(instruction)
                # Use updated value from memory if exists
                if opcode == 10 and self.memory[operand] != 0:
                    print(f"Using existing value for input at location {operand}: {self.memory[operand]}")
                self.execute(opcode, operand)
                self.overflow_check()
        print("CPU re-execution completed")
        print(self.memory)

    def fetch(self):
        if self.instruction_counter >= len(self.memory):
            self.running = False
            return None
        instruction = self.memory[self.instruction_counter]
        self.instruction_counter += 1
        print(f"Fetching instruction at index {self.instruction_counter - 1}: {instruction}")
        return instruction

    def decode(self, instruction):
        # Adjusted to decode two-digit opcodes
        opcode = instruction // 100  # Two-digit opcode
        operand = instruction % 100  # Two-digit operand
        print(f"Decoded instruction: opcode {opcode}, operand {operand}")
        return opcode, operand

    def execute(self, opcode, operand):
        if not (0 <= operand < len(self.memory)):
            print(f"Invalid memory access at {operand}. Halting execution.")
            self.halt()
            return
        print(f"Executing opcode {opcode} with operand {operand}")
        if opcode == 10:  # Input instruction
            if operand in self.inputs:
                # Use the input that was manually set by the user
                self.memory[operand] = self.inputs[operand]
                print(f"Using stored input for operand {operand}: {self.inputs[operand]}")
            else:
                self.read(operand)
        elif opcode == 11:
            self.write(operand)
        elif opcode == 20:
            self.load(operand)
        elif opcode == 21:
            self.store(operand)
        elif opcode == 30:
            self.add(operand)
        elif opcode == 31:
            self.subtract(operand)
        elif opcode == 32:
            self.divide(operand)
        elif opcode == 33:
            self.multiply(operand)
        elif opcode == 40:
            self.branch(operand)
        elif opcode == 41:
            self.branchneg(operand)
        elif opcode == 42:
            self.branchzero(operand)
        elif opcode == 43:
            self.halt()
        else:
            print(f"Invalid opcode: {opcode}")

    def read(self, operand):
        if operand in self.inputs:
            print(f"Using stored input for operand {operand}")
            self.memory[operand] = self.inputs[operand]
        else:
            print(f"Setting up for input at location {operand}")
            self.waiting_for_input = True
            self.input_operand = operand

    def continue_execution(self, value):
        print(f"Received input: {value} for location {self.input_operand}")
        self.memory[self.input_operand] = value
        self.inputs[self.input_operand] = value
        self.waiting_for_input = False
        print(f"Resuming execution, next instruction at index {self.instruction_counter}")
        self.run()

    def write(self, operand):
        value = self.memory[operand]
        self.write_outputs.append(value)
        print(f"WRITE: Memory[{operand}] = {value}")

    def load(self, operand):
        self.accumulator = self.memory[operand]
        print(f"Accumulator loaded with value: {self.accumulator}")

    def store(self, operand):
        self.memory[operand] = self.accumulator
        print(f"Stored accumulator value {self.accumulator} at memory location {operand}")

    def add(self, operand):
        self.accumulator += self.memory[operand]
        print(f"Accumulator after addition: {self.accumulator}")

    def subtract(self, operand):
        self.accumulator -= self.memory[operand]
        print(f"Accumulator after subtraction: {self.accumulator}")

    def divide(self, operand):
        if self.memory[operand] == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.accumulator //= self.memory[operand]
        print(f"Accumulator after division: {self.accumulator}")

    def multiply(self, operand):
        self.accumulator *= self.memory[operand]
        print(f"Accumulator after multiplication: {self.accumulator}")

    def branch(self, operand):
        self.instruction_counter = operand

    def branchneg(self, operand):
        if self.accumulator < 0:
            self.instruction_counter = operand

    def branchzero(self, operand):
        if self.accumulator == 0:
            self.instruction_counter = operand

    def halt(self):
        print("Halt command executed - stopping execution")
        self.running = False

    def display_memory(self):
        return str(self.memory)

    def overflow_check(self):
        if self.accumulator > 999999:
            self.accumulator = 999999
        elif self.accumulator < -999999:
            self.accumulator = -999999

