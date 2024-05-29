from uv_sim import UVSim


def main():
    """
    starts the UVSim application, initialize the simulator , load and execute it
    """
    uv_sim = UVSim()
    program_file = input("enter the path to BasiicML program file:")
    uv_sim.load_program_from_file(program_file)
    uv_sim.execute_program()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
