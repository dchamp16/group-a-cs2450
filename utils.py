def load_program(file_path):
    try:
        with open(file_path, 'r') as file:
            program = []
            for line in file:
                instruction = int(line.strip())
                program.append(instruction)
            return program
    except Exception as e:
        print(f"Error loading program: {e}")
        return None
