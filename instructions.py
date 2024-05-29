def read_instruction(uv_sim, operand):
    """
    reads a number from the user and stores it in specified location

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index where the input stored
    """
    pass


def write_instruction(uv_sim, operand):
    """
    writes the number from specied location to the output

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which will be outputted
    """
    pass


def load_instruction(uv_sim, operand):
    """
    load a number from specified location to accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to load the value
    """
    pass


def store_instruction(uv_sim, operand):
    """
    store the number from the accumulator to specified location

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which the accumulator value will be stored
    """
    pass



def add_instruction(uv_sim, operand):
    """
    subtract the number from a specified location from the accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to add the value
    """
    pass


def subtract_instruction(uv_sim, operand):
    """
    subtract the number from a specified location from the accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to subtract the value
    """
    pass


def divide_instruction(uv_sim, operand):
    """
    divide the number from a specified location from the accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to divide the value
    """
    pass


def multiply_instruction(uv_sim, operand):
    """
    multiply the number from a specified location from the accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to multiply the value
    """
    pass


def branch_instruction(uv_sim, operand):
    """
    # change the execution point to the specified location

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to branch
    """
    pass


def branchneg_instruction(uv_sim, operand):
    """
    if the accumulator is negative change the point to the specified location

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to branch if negative
    """
    pass


def branchzero_instruction(uv_sim, operand):
    """
    if the accumulator is zero change the point to the specified location

    parameters:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to branch if zero

    """
    pass
