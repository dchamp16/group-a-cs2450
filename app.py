from flask import Flask, render_template, request, redirect, url_for, flash, session
from uv_sim import UVSim
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a randomly generated key

# Initialize the simulator globally
uv_sim = UVSim()

@app.route('/', methods=['GET', 'POST'])
def index():
    global uv_sim
    message = ''
    input_prompt = ''

    if request.method == 'POST':
        if 'file' in request.files:
            files = request.files.getlist('file')
            uv_sim.reset()  # Reset the simulator state before loading new files
            for file in files:
                file_content = file.read().decode().strip()
                print(f"File content: {file_content}")  # Debug log
                program = [int(line.replace('+', '')) for line in file_content.split()]
                if program:
                    uv_sim.load_program(program)
                    print(f"Program loaded: {program}")  # Debug log
                    uv_sim.run()
                    print(f"Memory after run: {uv_sim.cpu.memory}")  # Debug log
                    if uv_sim.cpu.waiting_for_input:
                        message = 'Files loaded successfully. Waiting for input...'
                        session['input_step'] = 1  # Set to first input step
                    else:
                        message = 'Files loaded successfully. Program halted.'
                else:
                    flash('Error: Program is empty')
                    return redirect(url_for('index'))
            flash(message)
            return redirect(url_for('index'))
        elif 'user_input' in request.form:
            user_input = request.form['user_input']
            # Validate and process user input
            if not (user_input.lstrip('-').isdigit() and len(user_input.replace('-', '')) == 4 and -9999 <= int(user_input) <= 9999):
                flash('Please enter a 4-digit integer (or negative 4-digit integer).')
                return redirect(url_for('index'))
            uv_sim.cpu.continue_execution(int(user_input))
            print(f"Memory after input: {uv_sim.cpu.memory}")  # Debug log
            if uv_sim.cpu.waiting_for_input:
                if session.get('input_step') == 1:
                    session['input_step'] = 2  # Move to second input step
                    flash('Please enter the second input.')
                elif session.get('input_step') == 2:
                    session['input_step'] = 0  # Reset input step
                    flash('Input complete.')
                return redirect(url_for('index'))
            else:
                message = 'Program halted.'
                flash(message)
                return redirect(url_for('index'))

    message = request.args.get('message', '')
    memory = uv_sim.cpu.memory if uv_sim.cpu.memory else []
    input_required = uv_sim.cpu.waiting_for_input
    operand = uv_sim.cpu.input_operand if input_required else None
    input_prompt = ''
    if input_required:
        if session.get('input_step') == 1:
            input_prompt = 'first'
        elif session.get('input_step') == 2:
            input_prompt = 'second'
    return render_template('index.html', memory=memory, input_required=input_required, operand=operand, message=message, input_prompt=input_prompt, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
