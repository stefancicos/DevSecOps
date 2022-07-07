from flask import Flask
import subprocess
import ftplib
from flask import request
from waitress import serve

app = Flask(__name__)

def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/cmdinj/<cmd>')
def main(cmd):
	return run_cmd(cmd)

@app.route('/pyexecinj/<cmd>')
def pyexecinj(cmd):
	return str(exec(cmd))

@app.route('/pyevalinj/<cmd>')
def pyevalinj(cmd):
	return str(eval(cmd))

serve(app, port=8081, host='192.168.201.204')
