from flask import Flask, render_template, request, redirect, url_for, flash
from uv_sim import UVSim
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a randomly generated key

# Initialize the simulator globally
uv_sim = UVSim()

# Register the custom filter
@app.template_filter('enumerate')
def do_enumerate(iterable):
    return enumerate(iterable)

app.jinja_env.filters['enumerate'] = do_enumerate

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
                program = [int(line.replace('+', '')) for line in file_content.split()]
                if program:
                    uv_sim.load_program(program)
                    uv_sim.run()
                    if uv_sim.cpu.waiting_for_input:
                        message = 'Files loaded successfully. Waiting for input...'
                    else:
                        message = 'Files loaded successfully. Program halted.'
                else:
                    flash('Error: Program is empty')
                    return redirect(url_for('index'))
            flash(message)
            return redirect(url_for('index'))
        elif 'user_input' in request.form:
            user_input = request.form['user_input']
            if not user_input.isdigit() or len(user_input) != 4:
                flash('Please enter a 4-digit integer.')
                return redirect(url_for('index'))
            uv_sim.cpu.continue_execution(int(user_input))
            if uv_sim.cpu.running:
                return redirect(url_for('index'))
            else:
                message = 'Program halted.'
                flash(message)
                return redirect(url_for('index'))

    message = request.args.get('message', '')
    memory = uv_sim.cpu.memory if uv_sim.cpu.memory else []
    input_required = uv_sim.cpu.waiting_for_input
    operand = uv_sim.cpu.input_operand if input_required else None
    if input_required:
        input_prompt = 'first' if operand == 90 else 'second'
    return render_template('index.html', memory=memory, input_required=input_required, operand=operand, message=message, input_prompt=input_prompt)

if __name__ == '__main__':
    app.run(debug=True)
