import uv_sim
import utils

def main():
    print("Enter the path to BasicML program file:")
    file_path = input()
    
    program = utils.load_program(file_path)
    if program:
        print(f"Successfully loaded {len(program)} instructions into memory.")
    else:
        print("Failed to load program.")
        return
    
    sim = uv_sim.UVSim()
    sim.load_program(program)

    sim.run()

if __name__ == "__main__":
    main()
