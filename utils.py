def parse_instruction(instruction):
    op_code = instruction // 100
    operand = instruction % 100
    return op_code, operand

def read_program(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    program = [int(line.strip()) for line in lines]
    return program
