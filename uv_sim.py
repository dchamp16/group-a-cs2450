class UVSim:
    def __init__(self):
        self.memory = [0] * 100  # 100-word memory
        self.accumulator = 0  # This is the accumulator register
        self.instruction_counter = 0  # This is the instruction counter

    def load_program(self, program):
        for index, instruction in enumerate(program):
            self.memory[index] = instruction

    def fetch(self):
        instruction = self.memory[self.instruction_counter]
        self.instruction_counter += 1
        return instruction

    def decode(self, instruction):
        opcode = instruction // 100
        operand = instruction % 100
        return opcode, operand

    def execute(self, opcode, operand):
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

    def run(self):
        while True:
            instruction = self.fetch()
            opcode, operand = self.decode(instruction)
            print(f"Fetched instruction: {instruction}")
            print(f"Decoded to opcode: {opcode}, operand: {operand}")
            self.execute(opcode, operand)

    def read(self, operand):
        value = int(input("Enter a value: "))
        self.memory[operand] = value

    def write(self, operand):
        print(f"Value at memory location {operand}: {self.memory[operand]}")

    def load(self, operand):
        self.accumulator = self.memory[operand]

    def store(self, operand):
        self.memory[operand] = self.accumulator

    def add(self, operand):
        self.accumulator += self.memory[operand]

    def subtract(self, operand):
        self.accumulator -= self.memory[operand]

    def divide(self, operand):
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
        print("Program halted.")
        exit()
