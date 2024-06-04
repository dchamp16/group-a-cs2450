from uv_sim import UVSim


def main():
    """
    starts the UVSim application, initialize the simulator , load and execute it
    """
    uv_sim = UVSim()
    program_file = input("enter the path to BasicML program file:")
    uv_sim.load_program_from_file(program_file)
    uv_sim.execute_program()

    print(uv_sim.memory)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# This is a potential main too.
# from uv_sim import UVSim
# from utils import read_program

# def main():
#     file_path = input("Enter the path to the program file: ")
#     program = read_program(file_path)
#     simulator = UVSim()
#     simulator.load_program(program)
#     simulator.execute()

# if __name__ == "__main__":
#     main()
