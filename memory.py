class Memory:
    def __init__(self, size=100):
        self.cells = [0] * size

    def __getitem__(self, index):
        return self.cells[index]

    def __setitem__(self, index, value):
        self.cells[index] = value

    def __len__(self):
        return len(self.cells)

    def __str__(self):
        return '[' + ', '.join(str(mem) for mem in self.cells) + ']'
