from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from uv_sim import UVSim
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a randomly generated key

# Initialize the simulator globally
uv_sim = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global uv_sim
    message = ''
    input_prompt = ''

    if request.method == 'POST':
        if 'memory_size' in request.form:
            memory_size = int(request.form['memory_size'])
            uv_sim = UVSim(memory_size=memory_size)
            flash('Memory size updated successfully.')
            return redirect(url_for('index'))

        if 'user_input' in request.form:
            user_input = request.form['user_input']
            # Changed validation to allow six-digit integers
            if not (user_input.lstrip('-').isdigit() and len(user_input.replace('-', '')) <= 6 and -999999 <= int(user_input) <= 999999):
                flash('Please enter a valid 6-digit integer (or negative 6-digit integer).')
                return redirect(url_for('index'))
            uv_sim.cpu.continue_execution(int(user_input))
            if uv_sim.cpu.waiting_for_input:
                flash('Program running. Waiting for input...')
            else:
                flash('Program halted.')
            return redirect(url_for('index'))

    message = request.args.get('message', '')
    memory = uv_sim.cpu.memory if uv_sim and uv_sim.cpu.memory else []
    input_required = uv_sim and uv_sim.cpu.waiting_for_input
    operand = uv_sim.cpu.input_operand if input_required else None
    input_prompt = ''
    if input_required:
        if session.get('input_step') == 1:
            input_prompt = 'first'
        elif session.get('input_step') == 2:
            input_prompt = 'second'
    return render_template('index.html', memory=memory, input_required=input_required, operand=operand, message=message, input_prompt=input_prompt, enumerate=enumerate, write_outputs=uv_sim.cpu.write_outputs if uv_sim else [])

@app.route('/load', methods=['POST'])
def load():
    global uv_sim
    uv_sim.reset()  # Reset the simulator state before loading new files
    if 'file' in request.files:
        files = request.files.getlist('file')
        for file in files:
            file_content = file.read().decode().strip()
            print(f"File content: {file_content}")  # Debug log
            program = [int(line.replace('+', '')) for line in file_content.split()]

            # Error handling for memory overload
            if len(program) > len(uv_sim.memory):
                flash(f'Error: Program size ({len(program)}) exceeds memory capacity ({len(uv_sim.memory)}).')
                return redirect(url_for('index'))

            if program:
                uv_sim.load_program(program)
                print(f"Program loaded: {program}")  # Debug log
                flash('Files loaded successfully. You can now run the program.')
            else:
                flash('Error: Program is empty')
                return redirect(url_for('index'))
        return redirect(url_for('index'))
    else:
        flash('No file uploaded.')
        return redirect(url_for('index'))



@app.route('/run', methods=['POST'])
def run():
    global uv_sim
    uv_sim.run()
    if uv_sim.cpu.waiting_for_input:
        flash('Program running. Waiting for input...')
    else:
        flash('Program halted.')
    return redirect(url_for('index'))

@app.route('/update_memory', methods=['POST'])
def update_memory():
    data = request.get_json()
    memory_location = data.get('memory_location')
    instruction = data.get('instruction')
    if 0 <= memory_location < len(uv_sim.cpu.memory):
        try:
            instruction = int(instruction)
            # Changed validation to allow six-digit instructions
            if -999999 <= instruction <= 999999:
                uv_sim.cpu.memory[memory_location] = instruction
                return jsonify({'success': True})
            else:
                return jsonify({'success': False, 'error': 'Instruction out of bounds (-999999 to 999999)'}), 400
        except ValueError:
            return jsonify({'success': False, 'error': 'Invalid instruction format'}), 400
    return jsonify({'success': False, 'error': 'Invalid memory location'}), 400

if __name__ == '__main__':
    app.run(debug=True)
