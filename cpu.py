from memory import Memory

class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True

    def load_program(self, program):
        if len(program) > len(self.memory):
            print("Program size exceeds memory capacity")
            return False
        for index, instruction in enumerate(program):
            self.memory[index] = instruction
        print(f"Program loaded: {self.memory}")
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
            if opcode == 43:
                func()
            else:
                func(operand)
        else:
            print(f"Invalid opcode: {opcode}")

    def run(self):
        while self.running:
            instruction = self.fetch()
            if instruction is None:
                print("No more instructions or an error occurred.")
                break
            opcode, operand = self.decode(instruction)
            self.execute(opcode, operand)

    def read(self, operand):
        while True:
            value = input("Enter a 4-digit value: ")
            if value.isdigit() and len(value) == 4:
                self.memory[operand] = int(value)
                break
            else:
                print("Invalid input. Enter a 4-digit number.")

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
        print(f"Branching to instruction {operand}")
        self.instruction_counter = operand

    def branchneg(self, operand):
        if self.accumulator < 0:
            print(f"Branching to {operand} because accumulator is negative")
            self.instruction_counter = operand

    def branchzero(self, operand):
        if self.accumulator == 0:
            print(f"Branching to {operand} because accumulator is zero")
            self.instruction_counter = operand

    def halt(self):
        print("Program halted.")
        # exit()
        self.running = False

    def display_memory(self):
        # Create a string representation of the memory array
        return '[' + ', '.join(str(mem) for mem in self.memory) + ']'