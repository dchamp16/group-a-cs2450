def read_instruction(uv_sim, operand):
    """
    reads a number from the user and stores it in specified location

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index where the input stored
    """

    try:
        value = int(input("Enter and integer: "))
        uv_sim.memory[operand] = value
        print(f"stored {value} at location {operand}")
        return True
    except ValueError:
        print("Invalid input! enter valid integer")
        return False


def write_instruction(uv_sim, operand):
    """
    writes the number from specified location to the output

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which will be outputted
    """
    value = uv_sim.memory[operand]
    print(f"Value at location {operand} is {value}")
    return True


def load_instruction(uv_sim, operand):
    """
    load a number from specified location to accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to load the value
    """
    uv_sim.accumulator = uv_sim.memory[operand]
    print(f"Accumulator value {uv_sim.accumulator} at location {operand}")
    return True


def store_instruction(uv_sim, operand):
    """
    store the number from the accumulator to specified location

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which the accumulator value will be stored
    """
    uv_sim.memory[operand] = uv_sim.accumulator
    print(f"Accumulator value {uv_sim.accumulator} at location {operand}")
    return True


def add_instruction(uv_sim, operand):
    """
    subtract the number from a specified location from the accumulator

    parameter:
    uv_sim(UVSim): instance of the UVSim class
    operant(int): memory location index which to add the value
    """
    uv_sim.accumulator += uv_sim.memory[operand]
    print(f"Added value from location {operand} to accumulator at location {uv_sim.accumulator}")
    return True


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


def halt_instruction(uv_sim, operand):
    """
    Halts the execution of the program

    :param uv_sim (UVSim): the instance of UVSim class to operate the simulation
    :param operand (int): memory location not use in this function
    """
    print("Program halted.")
    return False  # To break the execution loop from execute_program
