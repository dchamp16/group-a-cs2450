from flask import Flask, render_template, request, redirect, url_for
from uv_sim import UVSim

app = Flask(__name__)

# Initialize the simulator globally
sim = UVSim()

@app.route('/', methods=['GET', 'POST'])
def index():
    global sim
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            file_content = file.read().decode().strip()
            print("File content:", file_content)  # Debug statement
            program = file_content.split()
            try:
                # Remove plus signs and convert to integers
                program = [int(line.replace('+', '')) for line in program]
                print("Loaded program:", program)  # Debug statement
                if not program:
                    print("Error: Program is empty")
                else:
                    sim.load_program(program)
                    sim.run()
            except ValueError as e:
                print("Error parsing program:", e)  # Debug statement
            return redirect(url_for('index'))
        elif 'user_input' in request.form:
            user_input = request.form['user_input']
            print("User input received:", user_input)  # Debug statement
            try:
                sim.cpu.continue_execution(int(user_input))
            except ValueError as e:
                print("Error with user input:", e)  # Debug statement
            return redirect(url_for('index'))

    memory = sim.cpu.display_memory() if sim.cpu.memory else []
    input_required = sim.cpu.waiting_for_input
    operand = sim.cpu.input_operand if input_required else None
    return render_template('index.html', memory=memory, input_required=input_required, operand=operand)

if __name__ == '__main__':
    app.run(debug=True)
