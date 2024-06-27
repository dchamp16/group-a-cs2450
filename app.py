from flask import Flask, render_template, request, redirect, url_for
from uv_sim import UVSim

app = Flask(__name__)

# Initialize the simulator globally
uv_sim = UVSim()

@app.route('/', methods=['GET', 'POST'])
def index():
    global uv_sim
    message = ''
    input_prompt = ''
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            file_content = file.read().decode().strip()
            program = [int(line.replace('+', '')) for line in file_content.split()]
            if program:
                uv_sim.load_program(program)
                uv_sim.run()
                message = 'File loaded successfully.'
            else:
                message = 'Error: Program is empty'
            return redirect(url_for('index', message=message))
        elif 'user_input' in request.form:
            user_input = request.form['user_input']
            uv_sim.cpu.continue_execution(int(user_input))
            if uv_sim.cpu.running:
                return redirect(url_for('index'))
            else:
                message = 'Program halted.'
                return redirect(url_for('index', message=message))

    message = request.args.get('message', '')
    memory = uv_sim.cpu.display_memory() if uv_sim.cpu.memory else []
    input_required = uv_sim.cpu.waiting_for_input
    operand = uv_sim.cpu.input_operand if input_required else None
    if input_required:
        input_prompt = 'Enter input for operand ' + str(operand)

    return render_template('index.html', memory=memory, input_required=input_required, operand=operand, message=message, input_prompt=input_prompt)

if __name__ == '__main__':
    app.run(debug=True)
