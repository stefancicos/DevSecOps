from flask import Flask
import subprocess
import ftplib
from flask import request
from waitress import serve

app = Flask(__name__)

def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/<cmd>')
def main(cmd):
	number = 9
	return run_cmd(cmd)+"<hr>"+exec("print('Hello World!\n')")+"<hr>"+eval("number * number")

serve(app, port=8081, host='0.0.0.0')
