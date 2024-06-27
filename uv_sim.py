from memory import Memory
from cpu import CPU

class UVSim:
    def __init__(self, memory_size=100):
        self.memory = [0] * memory_size
        self.cpu = CPU(self.memory)

    def load_program(self, program):
        self.cpu.load_program(program)

    def run(self):
        self.cpu.run()

    def reset(self):
        self.memory = [0] * len(self.memory)
        self.cpu = CPU(self.memory)
