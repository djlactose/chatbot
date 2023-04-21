from flask import Flask, request, jsonify, render_template_string
import subprocess
import shlex

app = Flask(__name__)

@app.route('/')
def index():
    with open("templates/index.html") as f:
        template = f.read()
    return render_template_string(template)

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form.get('command')
    sanitized_command = '/tmp/gpt4all-chat/ggml/build/bin/gpt-j -m /mnt/ggml-gpt4all-j.bin -n 200 --top_k 40 --top_p 0.9 -b 9 --temp 0.9 -p "' + shlex.quote(command) + '"'
    try:
        output = subprocess.check_output(sanitized_command, stderr=subprocess.STDOUT, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)