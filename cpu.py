class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True
        self.waiting_for_input = False
        self.input_operand = None

    def load_program(self, program):
        if len(program) > len(self.memory):
            raise ValueError("Program size exceeds memory capacity")
        self.memory[:len(program)] = program
        self.instruction_counter = 0
        print("Program loaded into memory:", self.memory)  # Debug statement

    def run(self):
        while self.running:
            if not self.waiting_for_input:
                instruction = self.fetch()
                if instruction is not None:
                    opcode, operand = self.decode(instruction)
                    self.execute(opcode, operand)
            else:
                print("Waiting for input...")
                break
        if self.waiting_for_input:
            print("Execution paused for input.")

    def fetch(self):
        if self.instruction_counter >= len(self.memory):
            self.running = False
            return None
        instruction = self.memory[self.instruction_counter]
        self.instruction_counter += 1
        print(f"Fetching instruction at index {self.instruction_counter - 1}: {instruction}")
        return instruction

    def decode(self, instruction):
        opcode = instruction // 100
        operand = instruction % 100
        print(f"Decoded instruction: opcode {opcode}, operand {operand}")
        return opcode, operand

    def execute(self, opcode, operand):
        print(f"Executing opcode {opcode} with operand {operand}")
        if opcode == 10:
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
        print(f"Setting up for input at location {operand}")
        self.waiting_for_input = True
        self.input_operand = operand

    def write(self, operand):
        print(f"Memory[{operand}]: {self.memory[operand]}")

    def load(self, operand):
        self.accumulator = self.memory[operand]

    def store(self, operand):
        self.memory[operand] = self.accumulator

    def add(self, operand):
        self.accumulator += self.memory[operand]
        print(f"Accumulator after addition: {self.accumulator}")

    def subtract(self, operand):
        self.accumulator -= self.memory[operand]

    def divide(self, operand):
        if self.memory[operand] == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.accumulator //= self.memory[operand]

    def multiply(self, operand):
        self.accumulator *= self.memory[operand]

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
        print(f"Running status after halt: {self.running}")  # Check if it sets correctly

    def continue_execution(self, value):
        print(f"Received input: {value} for location {self.input_operand}")
        self.memory[self.input_operand] = value
        self.waiting_for_input = False
        print(f"Resuming execution, next instruction at index {self.instruction_counter}")
        self.run()

    def display_memory(self):
        return str(self.memory)
