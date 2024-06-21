from memory import Memory

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
        self.running = True
        while self.running:
            instruction = self.fetch()
            if instruction is None:
                break
            opcode, operand = self.decode(instruction)
            print(f"Executing instruction: {instruction}, Opcode: {opcode}, Operand: {operand}")  # Debug statement
            self.execute(opcode, operand)

    def fetch(self):
        if self.instruction_counter >= len(self.memory):
            self.running = False
            return None
        instruction = self.memory[self.instruction_counter]
        self.instruction_counter += 1
        return instruction

    def decode(self, instruction):
        opcode = instruction // 100
        operand = instruction % 100
        return opcode, operand

    def execute(self, opcode, operand):
        operations = {
            10: self.read,
            11: self.write,
            20: self.load,
            21: self.store,
            30: self.add,
            31: self.subtract,
            32: self.divide,
            33: self.multiply,
            40: self.branch,
            41: self.branchneg,
            42: self.branchzero,
            43: self.halt
        }
        func = operations.get(opcode)
        if func:
            func(operand)

    def read(self, operand):
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

    def halt(self, operand):
        self.running = False

    def continue_execution(self, value):
        self.memory[self.input_operand] = value
        self.waiting_for_input = False
        self.run()

    def display_memory(self):
        return str(self.memory)
