from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import uv_sim
import utils

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            program = utils.load_program(file)
            if program:
                sim = uv_sim.UVSim()
                sim.load_program(program)
                sim.run()
                memory = sim.cpu.display_memory()
                return render_template('index.html', memory=memory)
            else:
                return render_template('index.html', error="Failed to load program.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
