from memory import Memory
from cpu import CPU

class UVSim:
    def __init__(self):
        self.memory = Memory(100)
        self.cpu = CPU(self.memory)

    def load_program(self, program):
        return self.cpu.load_program(program)

    def run(self):
        self.cpu.run()
