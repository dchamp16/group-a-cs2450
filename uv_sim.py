class UVSim:
    def __init__(self):
        self.memory = [0] * 100  # 100-word memory
        self.accumulator = 0  # This is the accumulator register
        self.instruction_counter = 0  # This is the instruction counter
        self.running = True

    def load_program(self, program):
        if len(program) > len(self.memory):
            print("Program size exceeds memory capacity")
            return False
        for index, instruction in enumerate(program):
            self.memory[index] = instruction
        return True

    def fetch(self):
        if self.instruction_counter >= len(self.memory):
            print("Instruction counter out of memory bounds")
            self.halt()
            return None
        instruction = self.memory[self.instruction_counter]
        self.instruction_counter += 1
        return instruction

    def decode(self, instruction):
        if instruction is None:
            return None, None
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
        else:
            print(f"Invalid opcode: {opcode}")

    # def run(self):
    #     while True:
    #         instruction = self.fetch()
    #         opcode, operand = self.decode(instruction)
    #         print(f"Fetched instruction: {instruction}")
    #         print(f"Decoded to opcode: {opcode}, operand: {operand}")
    #         self.execute(opcode, operand)
    # self.display_memory() # optional to display memory state

    def run(self):
        while self.running:
            instruction = self.fetch()
            if instruction is None:  # Properly handle None before decoding
                print("No more instructions or an error occurred.")
                break
            opcode, operand = self.decode(instruction)
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
        if self.memory[operand] == 0:
            print("Cannot divide by zero")
            self.halt()
        else:
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
        # exit()
        self.running = False

    def display_memory(self):
        # Create a string representation of the memory array
        return '[' + ', '.join(str(mem) for mem in self.memory) + ']'

