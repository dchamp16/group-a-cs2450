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


# class Instructions:
#     READ = 10
#     WRITE = 11
#     LOAD = 20
#     STORE = 21
#     ADD = 30
#     SUBTRACT = 31
#     DIVIDE = 32
#     MULTIPLY = 33
#     BRANCH = 40
#     BRANCHNEG = 41
#     BRANCHZERO = 42
#     HALT = 43

# def read_instruction(uv_sim, operand):
#     """
#     Reads a number from the user and stores it in specified location.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index where the input stored
#     """
#     try:
#         value = int(input("Enter an integer: "))
#         uv_sim.memory[operand] = value
#         print(f"Stored {value} at location {operand}")
#         return True
#     except ValueError:
#         print("Invalid input! Enter a valid integer")
#         return False

# def write_instruction(uv_sim, operand):
#     """
#     Writes the number from specified location to the output.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which will be outputted
#     """
#     value = uv_sim.memory[operand]
#     print(f"Value at location {operand} is {value}")
#     return True

# def load_instruction(uv_sim, operand):
#     """
#     Loads a number from specified location to accumulator.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which to load the value
#     """
#     uv_sim.accumulator = uv_sim.memory[operand]
#     print(f"Accumulator value {uv_sim.accumulator} at location {operand}")
#     return True

# def store_instruction(uv_sim, operand):
#     """
#     Stores the number from the accumulator to specified location.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which the accumulator value will be stored
#     """
#     uv_sim.memory[operand] = uv_sim.accumulator
#     print(f"Stored accumulator value {uv_sim.accumulator} at location {operand}")
#     return True

# def add_instruction(uv_sim, operand):
#     """
#     Adds a number from specified location to the accumulator.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which to add the value
#     """
#     uv_sim.accumulator += uv_sim.memory[operand]
#     print(f"Accumulator value after addition: {uv_sim.accumulator}")
#     return True

# def subtract_instruction(uv_sim, operand):
#     """
#     Subtracts a number from specified location from the accumulator.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which to subtract the value
#     """
#     uv_sim.accumulator -= uv_sim.memory[operand]
#     print(f"Accumulator value after subtraction: {uv_sim.accumulator}")
#     return True

# def divide_instruction(uv_sim, operand):
#     """
#     Divides the accumulator by a number from specified location.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which to divide the value
#     """
#     if uv_sim.memory[operand] != 0:
#         uv_sim.accumulator //= uv_sim.memory[operand]
#         print(f"Accumulator value after division: {uv_sim.accumulator}")
#         return True
#     else:
#         print("Error: Division by zero")
#         return False

# def multiply_instruction(uv_sim, operand):
#     """
#     Multiplies a number from specified location with the accumulator.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index which to multiply the value
#     """
#     uv_sim.accumulator *= uv_sim.memory[operand]
#     print(f"Accumulator value after multiplication: {uv_sim.accumulator}")
#     return True

# def branch_instruction(uv_sim, operand):
#     """
#     Branches to a specified memory location.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index to branch to
#     """
#     uv_sim.instruction_counter = operand
#     return True

# def branch_neg_instruction(uv_sim, operand):
#     """
#     Branches to a specified memory location if accumulator is negative.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index to branch to
#     """
#     if uv_sim.accumulator < 0:
#         uv_sim.instruction_counter = operand
#     return True

# def branch_zero_instruction(uv_sim, operand):
#     """
#     Branches to a specified memory location if accumulator is zero.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index to branch to
#     """
#     if uv_sim.accumulator == 0:
#         uv_sim.instruction_counter = operand
#     return True

# def halt_instruction(uv_sim, operand):
#     """
#     Halts the program execution.

#     parameter:
#     uv_sim(UVSim): instance of the UVSim class
#     operand(int): memory location index (not used)
#     """
#     uv_sim.halted = True
#     return True
