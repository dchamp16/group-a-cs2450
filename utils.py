def load_program(file_stream):
    try:
        program = []
        for line in file_stream:
            instruction = int(line.strip())
            program.append(instruction)
        return program
    except Exception as e:
        print(f"Error loading program: {e}")
        return None
